# -*- coding: utf-8 -*-
"""Functionality that extends on what the base StatsCan api returns in some way

TODO
----
Function to delete tables

Extend getChangedCubeList with a function that returns all tables updated
within a date range
"""
import os
import json
import zipfile
import h5py
import pandas as pd
import numpy as np
import requests
import tqdm 
# from stats_can.scwds import get_series_info_from_vector
# from stats_can.scwds import get_data_from_vectors_and_latest_n_periods
# from stats_can.scwds import get_bulk_vector_data_by_range
# from stats_can.scwds import get_cube_metadata
# from stats_can.scwds import get_full_table_download
# from stats_can.helpers import parse_tables
# from stats_can.helpers import parse_vectors


def get_tables_for_vectors(vectors):
    """ get a list of dicts mapping vectors to tables

    Parameters
    ----------
    vectors : list of str or str
        Vectors to find tables for

    Returns
    -------
    tables_list: list of dict
        keys for each vector number return the table, plus a key for
        'all_tables' that has a list of unique tables used by vectors
    """
    v_json = get_series_info_from_vector(vectors)
    vectors = [j['vectorId'] for j in v_json]
    tables_list = {j['vectorId']: str(j['productId']) for j in v_json}
    tables_list['all_tables'] = []
    for vector in vectors:
        if tables_list[vector] not in tables_list['all_tables']:
            tables_list['all_tables'].append(tables_list[vector])
    return tables_list


def table_subsets_from_vectors(vectors):
    """get a list of dicts mapping tables to vectors

    Parameters
    ----------
    vectors : list of str or str
        Vectors to find tables for

    Returns
    -------
    tables_dict: list of dict
        keys for each table used by the vectors, matched to a list of vectors
    """
    start_tables_dict = get_tables_for_vectors(vectors)
    tables_dict = {t: [] for t in start_tables_dict['all_tables']}
    vecs = list(start_tables_dict.keys())[:-1]  # all but the all_tables key
    for vec in vecs:
        tables_dict[start_tables_dict[vec]].append(vec)
    return tables_dict


def download_tables(tables, path=None, csv=True):
    """Download a json file and zip of data for a list of tables to path

    Parameters
    ----------
    tables: list of str
        tables to be downloaded
    path: str, default: None (will do current directory)
        Where to download the table and json
    csv: boolean, default True
        download in CSV format, if not download SDMX

    Returns
    -------
    downloaded: list
        list of tables that were downloaded
    """
    metas = get_cube_metadata(tables)
    size=len(metas)
    for i in tqdm.trange(size, desc='Downloading Dataset'):# For each soup
        sleep(0.001)
        product_id = metas[i]['productId']
        zip_url = get_full_table_download(product_id, csv=csv)
        if csv:
            zip_file = product_id + '-eng.zip'
        else:
            zip_file = product_id + '.zip'
        json_file = product_id + '.json'
        if path:
            zip_file = os.path.join(path, zip_file)
            json_file = os.path.join(path, json_file)
        # Thanks http://evanhahn.com/python-requests-library-useragent/
        response = requests.get(
            zip_url,
            stream=True,
            headers={'user-agent': None}
            )
        # Thanks https://bit.ly/2sPYPYw
        with open(json_file, 'w') as outfile:
            json.dump(metas[i], outfile)
        with open(zip_file, 'wb') as handle:
            for chunk in response.iter_content(chunk_size=512):
                if chunk:  # filter out keep-alive new chunks
                    handle.write(chunk)
    downloaded = [metas[i]['productId'] for meta in metas]
    return downloaded


def zip_update_tables(path=None, csv=True):
    """check local json, update zips of outdated tables

    Grabs the json files in path, checks them against the metadata on
    StatsCan and grabs updated tables where there have been changes
    There isn't actually a "last modified date" part to the metadata
    What I'm doing is comparing the latest reference period. Almost all
    data changes will at least include incremental releases, so this should
    capture what I want

    Parameters
    ----------
    path: str, default: None
        where to look for tables to update
    csv: boolean, default: True
        Downloads updates in CSV form by default, SDMX if false

    Returns
    -------
    update_table_list: list
        list of the tables that were updated

    """
    local_jsons = list_zipped_tables(path=path)
    tables = [j['productId'] for j in local_jsons]
    remote_jsons = get_cube_metadata(tables)
    update_table_list = []
    for local, remote in zip(local_jsons, remote_jsons):
        if local['cubeEndDate'] != remote['cubeEndDate']:
            update_table_list.append(local['productId'])
    download_tables(update_table_list, path, csv=csv)
    return update_table_list


def zip_table_to_dataframe(table, path=None):
    """Reads a StatsCan table into a pandas DataFrame

    If a zip file of the table does not exist in path, downloads it

    Parameters
    ----------
    table: str
        the table to load to dataframe from zipped csv
    path: str, default: current working directory when module is loaded
        where to download the tables or load them

    Returns:
    df: pandas.DataFrame
        the table as a dataframe
    """
    # Parse tables returns a list, can only do one table at a time here though
    print("PARSING DATA AS PANDAS DATAFRAME")
    table = parse_tables(table)[0]
    table_zip = table + '-eng.zip'
    if path:
        table_zip = os.path.join(path, table_zip)
    if not os.path.isfile(table_zip):
        download_tables([table], path)
    csv_file = table + '.csv'
    with zipfile.ZipFile(table_zip) as myzip:
        with myzip.open(csv_file) as myfile:
            col_names = pd.read_csv(myfile, nrows=0).columns
        # reopen the file or it misses the first row
        with myzip.open(csv_file) as myfile:
            types_dict = {'VALUE': float}
            types_dict.update(
                {col: str for col in col_names if col not in types_dict}
                )
            df = pd.read_csv(
                myfile,
                dtype=types_dict
                )

    possible_cats = [
        'GEO', 'DGUID', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS',
        'UOM', 'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE',
        'Wages', 'National Occupational Classification for Statistics (NOC-S)',
        'Supplementary unemployment rates', 'Sex', 'Age group',
        'Labour force characteristics', 'Statistics', 'Data type',
        'Job permanency', 'Union coverage', 'Educational attainment'
        ]
    actual_cats = [col for col in possible_cats if col in col_names]
    df[actual_cats] = df[actual_cats].astype('category')
    try:
        df['REF_DATE'] = pd.to_datetime(df['REF_DATE'], format='%Y-%m')
    except TypeError:
        df['REF_DATE'] = pd.to_datetime(df['REF_DATE'])
    return df


def list_zipped_tables(path=None):
    """List StatsCan tables available

    defaults to looking in the current working directory and for zipped CSVs

    Parameters
    ----------
    path: string or path, default None
        Where to look for zipped tables
    csv: boolean, default True
        Whether to look for CSV or SDMX files
    
    Returns
    -------
    tables: list
        list of available tables json data
    """
    # Find json files
    jsons = [f for f in os.listdir(path) if f.endswith('.json')]
    if path:
        jsons = [os.path.join(path, j) for j in jsons]
    tables = []
    for j in jsons:
        try:
            with open(j) as json_file:
                result = json.load(json_file)
                if 'productId' in result:
                    tables.append(result)
        except ValueError as e:
            print('failed to read json file' + j)
            print(e)
    return tables

        
def tables_to_h5(tables, h5file='stats_can.h5', path=None):
    """Take a table and its metadata and put it in an hdf5 file

    Parameters
    ----------
    tables: list of str
        tables to add to the h5file
    h5file: str, default stats_can.h5
        name of the h5file to store the tables in
    path: str or path, default = current working directory
        path to the h5file
    
    Returns
    -------
    tables: list
        list of tables loaded into the file
    """
    if path:
        h5file = os.path.join(path, h5file)
    tables = parse_tables(tables)
    for table in tables:
        hkey = 'table_' + table
        jkey = 'json_' + table
        zip_file = table + '-eng.zip'
        json_file = table + '.json'
        if path:
            zip_file = os.path.join(path, zip_file)
            json_file = os.path.join(path, json_file)
        if not os.path.isfile(json_file):
            download_tables([table], path)
        df = zip_table_to_dataframe(table, path=path)
        with open(json_file) as f_name:
            df_json = json.load(f_name)
        df.to_hdf(h5file, key=hkey, format='table', complevel=1)
        with h5py.File(h5file, 'a') as hfile:
            if jkey in hfile.keys():
                del hfile[jkey]
            hfile.create_dataset(jkey, data=json.dumps(df_json))
        os.remove(zip_file)
        os.remove(json_file)
    return tables


def table_from_h5(table, h5file='stats_can.h5', path=None):
    """Read a table from h5 to a dataframe

    Parameters
    ----------
    table: str
        name of the table to read
    h5file: str, default stats_can.h5
        name of the h5file to retrieve the table from
    path: str or path, default = current working directory
        path to the h5file

    Returns
    -------
    df: pd.DataFrame
        table in dataframe format
    """
    table = 'table_' + parse_tables(table)[0]
    if path:
        h5 = os.path.join(path, h5file)
    else:
        h5 = h5file
    try:
        df = pd.read_hdf(h5, key=table)
    except KeyError:
        print("Downloading and loading " + table)
        tables_to_h5(tables=table, h5file=h5file, path=path)
        df = pd.read_hdf(h5, key=table)
    return df


def metadata_from_h5(tables, h5file='stats_can.h5', path=None):
    """Read table metadata from h5

    Parameters
    ----------
    table: str or list of str
        name of the tables to read
    h5file: str, default stats_can.h5
        name of the h5file to retrieve the table from
    path: str or path, default = current working directory
        path to the h5file

    Returns
    -------
    list of local table metadata
    """
    if path:
        h5file = os.path.join(path, h5file)
    tables = ['json_' + tbl for tbl in parse_tables(tables)]
    jsons = []
    with h5py.File(h5file, 'r') as f:
        for tbl in tables:
            try:
                table_json = json.loads(f[tbl][()])
                jsons += [table_json]
            except KeyError:
                print("Couldn't find table " + tbl)
    return jsons


def list_h5_tables(path=None, h5file='stats_can.h5'):
    """return a list of metadata for StatsCan tables from an hdf5 file

    Parameters
    ----------
    path: str or path, default = current working directory
        path to the h5 file
    h5file: str, default stats_can.h5
        name of the h5file to read table data from
    
    Returns
    -------
    jsons: list
        list of available tables json data
    """
    keys = h5_included_keys(h5file=h5file, path=path)
    tables = parse_tables([k for k in keys if k.startswith('json_')])
    jsons = metadata_from_h5(tables, h5file=h5file, path=path)
    return jsons


def list_downloaded_tables(path=None, h5file='stats_can.h5'):
    """Return a list of metadata for StatsCan tables

    Wrapper for list zipped tables and list h5 tables

    Parameters
    ----------
    path: str or path, default = current working directory
        path to the h5 file
    h5file: str, default stats_can.h5
        name of the h5file to read table data from
    
    Returns
    -------
    jsons: list
        list of available tables json data
    """
    if h5file:
        jsons = list_h5_tables(path=path, h5file=h5file)
    else:
        jsons = list_zipped_tables(path=path)
    return jsons

def h5_update_tables(h5file='stats_can.h5', path=None, tables=None):
    """update any stats_can tables contained in an h5 file

    Parameters
    ----------
    h5file: str, default stats_can.h5
        name of the h5file to store the tables in
    path: str or path, default = current working directory
        path to the h5file
    tables: str or list of str, optional, default None
        If included will only update the subset of tables already in the file
        and in the tables parameter
    """
    if tables:
        local_jsons = metadata_from_h5(tables, h5file=h5file, path=path)
    else:
        if path:
            h5 = os.path.join(path, h5file)
        else:
            h5 = h5file
        with h5py.File(h5) as f:
            keys = [key for key in f.keys() if key.startswith('json')]
            local_jsons = [json.loads(f[key][()]) for key in keys]
    tables = [j['productId'] for j in local_jsons]
    remote_jsons = get_cube_metadata(tables)
    update_table_list = []
    for local, remote in zip(local_jsons, remote_jsons):
        if local['cubeEndDate'] != remote['cubeEndDate']:
            update_table_list.append(local['productId'])
    tables_to_h5(update_table_list, h5file=h5file, path=path)
    return update_table_list


def update_tables(path=None, h5file='stats_can.h5', tables=None, csv=True):
    """Update downloaded tables where required

    Reads local metadata, either from json files or stored in an h5 file,
    compares it to the metadata on the StatsCan website and downloads those
    tables that don't have matching metadata

    Just a wrapper for zip_update tables and h5_update_tables functions

    Parameters
    ----------
    path: str or path, default None
        Path where local tables are stored, assumes current directory if None
    h5file: str, default 'stats_can.h5'
        Name of the h5 file storing StatsCan tables, set to None for zips
    tables: list of str, default None
        For hdf5 only, update only a subset of tables that are both in the file
        and specified by this argument, None means update all tables
    csv: boolean, default True
        If updating zips this determines whether to update zipped CSV or SDMX
    
    Returns
    -------
    update_table_list: list of str
        list of updated tables
    """
    if h5file:
        return h5_update_tables(
            h5file=h5file,
            path=path,
            tables=tables
        )
    else:
        return zip_update_tables(path=path, csv=csv)


def h5_included_keys(h5file='stats_can.h5', path=None):
    """Return a list of keys in an h5 file

    Parameters
    ----------
    h5file: str, default stats_can.h5
        name of the h5file to store the tables in
    path: str or path, default = current working directory
        path to the h5file

    Returns
    -------
    keys: list
        list of keys in the hdf5 file
    """
    if path:
        h5file = os.path.join(path, h5file)
    with h5py.File(h5file, 'r') as f:
        keys = [key for key in f.keys()]
    return keys


def delete_tables(tables, path=None, h5file='stats_can.h5', csv=True):
    """Delete downloaded tables

    Parameters
    ----------
    tables: list
        list of tables to delete
    path: str or os path object, default None
        where to look for the tables to delete
    h5file: str default stats_can.h5
        h5file to remove from, set to None to remove zips
    csv: boolean, default True
        if h5file is None this specifies whether to delete zipped csv or SDMX
    
    Returns
    -------
    to_delete: list
        list of deleted tables
    """
    clean_tables = parse_tables(tables)
    available_tables_jsons = list_downloaded_tables(path=path, h5file=h5file)
    available_tables = [j['productId'] for j in available_tables_jsons]
    to_delete = [t for t in clean_tables if t in available_tables]
    if h5file:
        keys_to_del = []
        for td in to_delete:
            json_to_del = 'json_' + td
            tbl_to_del = 'table_' + td
            keys_to_del.append(json_to_del)
            keys_to_del.append(tbl_to_del)
        if path:
            h5file = os.path.join(path, h5file)
        with h5py.File(h5file, 'a') as f:
            for k in keys_to_del:
                del f[k]
    else:
        files_to_del = []
        for td in to_delete:
            json_to_del = td + '.json'
            if csv:
                zip_to_del = td + '-eng.zip' 
            else:
                zip_to_del = td + '.zip'
            files_to_del.append(zip_to_del)
            files_to_del.append(json_to_del)
        if path:
            files_to_del = [os.path.join(path, f) for f in files_to_del]
        for file in files_to_del:
            if os.path.exists(file):
                os.remove(file)
    return to_delete
    

def table_to_df(table, path=None, h5file='stats_can.h5'):
    """Read a table to a dataframe

    Wrapper for table_from_h5 and zip_table_to_dataframe

    Parameters
    ----------
    table: str
        name of the table to read
    h5file: str, default stats_can.h5
        name of the h5file to retrieve the table from, None for zip
    path: str or path, default = current working directory
        path to the table data

    Returns
    -------
    df: pd.DataFrame
        table in dataframe format
    """
    if h5file:
        df = table_from_h5(table=table, h5file=h5file, path=path)
    else:
        df = zip_table_to_dataframe(table=table, path=path)
    return df


def vectors_to_df(
    vectors, periods=1, start_release_date=None, end_release_date=None
):
    """data frame of vectors with n periods data or over range of release dates

    Wrapper on get_bulk_vector_data_by_range and
    get_data_from_vectors_and_latest_n_periods function to turn the resulting
    list of JSONs into a DataFrame

    Parameters
    ----------
    vectors: str or list of str
        vector numbers to get info for
    periods: int
        number of periods to retrieve data for
    start_release_date: datetime.date
        start release date for the data
    end_release_date: datetime.date
        end release date for the data

    Returns
    -------
    df: DataFrame
        vectors as columns and ref_date as the index (not release date)
    """
    df = pd.DataFrame()
    if ((end_release_date is None) | (start_release_date is None)):
        start_list = get_data_from_vectors_and_latest_n_periods(
            vectors, periods
            )
    else:
        start_list = get_bulk_vector_data_by_range(
            vectors, start_release_date, end_release_date
            )
    for vec in start_list:
        name = "v" + str(vec['vectorId'])
        ser = (
            pd.DataFrame(vec['vectorDataPoint'])
            .assign(refPer=lambda x: pd.to_datetime(x['refPer']))
            .set_index('refPer')
            .rename(columns={'value': name})
            .filter([name])
        )
        df = pd.concat([df, ser], axis=1, sort=True)
    return df


def vectors_to_df_local(
    vectors, path=None, start_date=None, h5file='stats_can.h5'
):
    """Make a dataframe with vector columns indexed on date from local data

    Parameters
    ----------
    vectors: list
        list of vectors to be read in
    path: str or os path, default None
        path to StatsCan tables
    start_date: datetime, optional, default None
        optional earliest reference date to include
    h5file: str, default stats_can.h5
        if specified will extract dataframes from an hdf5file instead of
        zipped csv tables
    
    """
    # Preserve an initial copy of the list for ordering, parsed and then
    # converted to string for consistency in naming
    vectors_ordered = parse_vectors(vectors)
    vectors_ordered = ['v' + str(v) for v in vectors_ordered]
    table_vec_dict = table_subsets_from_vectors(vectors)
    tables = list(table_vec_dict.keys())
    tables_dfs = {}
    columns = ['REF_DATE', 'VECTOR', 'VALUE']
    if h5file:
        meta = metadata_from_h5(
            tables,
            h5file=h5file,
            path=path
        )
        existing_tables = [t['productId'] for t in meta]
        to_download_tables = list(set(tables) - set(existing_tables))
        tables_to_h5(
            to_download_tables,
            h5file=h5file,
            path=path
            )
    for table in tables:
        if h5file:
            tables_dfs[table] = table_from_h5(
                table, h5file=h5file, path=path
                )[columns]
        else:
            tables_dfs[table] = zip_table_to_dataframe(table, path)[columns]
        df = tables_dfs[table]  # save me some typing
        vec_list = ['v' + str(v) for v in table_vec_dict[table]]
        df = df[df['VECTOR'].isin(vec_list)]
        if start_date is not None:
            start_date = np.datetime64(start_date)
            df = df[df['REF_DATE'] >= start_date]
        df = df.pivot(index='REF_DATE', columns='VECTOR', values='VALUE')
        df.columns = list(df.columns)  # remove categorical index
        tables_dfs[table] = df
    final_df = tables_dfs[tables[0]]
    for table in tables[1:]:
        final_df = pd.merge(
            final_df, tables_dfs[table],
            how='outer',
            left_index=True, right_index=True
            )
    final_df = final_df[vectors_ordered]
    return final_df


