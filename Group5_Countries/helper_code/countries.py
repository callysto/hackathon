import pandas as pd
import urllib

import matplotlib.pyplot as plt
import geopandas as gpd
from pylab import rcParams

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world = world[["name","geometry"]]

colors20 = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', 
          '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', 
          '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']

def get_countries_geometry(countries):
    countries.loc[countries["country"]=="United States", ["country"]] = "United States of America"
    result = world.merge(countries, left_on = 'name', right_on = 'country')
    result = result.drop(['name'], axis=1)
    return result

