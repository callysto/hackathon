import pandas as pd
import urllib
import matplotlib.pyplot as plt
import geopandas as gpd
from pylab import rcParams

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[["name","geometry"]]


def get_countries_geometry(countries):
    countries.loc[countries["country"]=="United States", ["country"]] = "United States of America"
    result = world.merge(countries, left_on = 'name', right_on = 'country')
    result = result.drop(['name'], axis=1)
    return result

