import chart_studio.plotly as py 

def get_average_by_artist(df,year,artist_list):
    music = df[df["year"]==year]
    music = music.drop(['year'], axis=1)
    result = pd.concat([music.groupby("artists").mean().loc[artist_list],music.mean().reset_index(name="All data").set_index("index").T])
    result.index += '_avg'+str(year)
    
    return result

def get_data_by_year(music,value):
    subset = music[[value,"year"]]
    result = pd.concat({k: g.reset_index(drop=True) for k, g in  subset.groupby('year')[value]}, axis=1)
    return result
