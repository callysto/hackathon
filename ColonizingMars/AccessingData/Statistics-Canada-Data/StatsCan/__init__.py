'''Read StatsCan Data into python, mostly pandas dataframes

TODO
----
Logging

French support
'''
__version__ = '2.0'
from stats_can import sc
from stats_can.scwds import get_changed_series_list
from stats_can.scwds import get_changed_cube_list
from stats_can.scwds import get_cube_metadata
from stats_can.scwds import get_series_info_from_vector
from stats_can.sc import table_to_df
from stats_can.sc import update_tables
from stats_can.sc import list_downloaded_tables
from stats_can.sc import delete_tables
from stats_can.sc import vectors_to_df
from stats_can.sc import vectors_to_df_local
