import pandas as pd
import urllib

import plotly.plotly as py
import cufflinks as cf


colors20 = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', 
          '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', 
          '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']

def get_counts_by_group(df, value):
    result = df.groupby(["Year",value]).size().reset_index(name="count")

    result = result.pivot(index="Year",columns=value, values="count").reset_index().\
                         rename_axis(None,axis="columns").set_index("Year")
    return result

def get_counts_by_medal(df):
    result = df.groupby(["Medal", "Sport"]).size().reset_index(name="count").\
                                     pivot(index="Sport", columns='Medal',values="count").reset_index().\
                                    rename_axis(None,axis="columns").set_index("Sport")
    return result


def get_participation_counts(df,year, season, country):
    data_season  = df[(df["Season"]==season) &(df["Year"]==year) &(df["region"]==country)]
    
    medals_season = data_season.dropna(subset=["Medal"])
    no_medals_season = data_season[data_season["Medal"].isna() ]
    
    df1 = no_medals_season.groupby(["Sport"]).size().reset_index(name="no medal").set_index("Sport")
    df2 = medals_season.groupby(["Sport"]).size().reset_index(name="medal").set_index("Sport")

    summary = pd.merge(df1,df2, how = "outer", left_index=True, right_index=True)
    
    return summary