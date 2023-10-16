"""TODO: 
    - EVERYTHING
    """

import json
import pandas as pd
import geopandas as gpd
import numpy as np
import folium as fol
import openpyxl
import data_manipulator

"""Our actual maps need to be GeoJson maps, not choropleths, 
    because choropleths do not allow for tooltips. Tooltips
    are the popups that show the data, like county name, 
    population, percent change, etc. -Clifton"""

"""Also, we need to figure out how to take care of the color
    scale problem, if it is still a problem when we create the
    new maps with the limits we have set like top 20 counties,
    etc. If we are still having that problem, we may have to
    inject HTML over the map, which is possible to do with
    folium. -Clifton"""


with open('/workspaces/Transportation-Flow-Analysis/Prototype/us-counties.json', 'r') as countiesJson:
    countiesGeoJson = json.load(countiesJson)

def main():
    test = data_manipulator()
    return 0

main