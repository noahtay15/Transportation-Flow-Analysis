import pandas as pd
import folium as fol
import os
import requests
import json


map = fol.Map(location=(40, -100),
        control_scale=True, 
        zoom_control=False, 
        zoom_start=6)

with open('us-counties.json', 'r') as countiesJson:
    USCounties = json.load(countiesJson)

fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=0.3, 
    line_weight=2
).add_to(map)


#downloadsDir = os.path.expanduser("~" + os.sep + "Downloads")
#html = os.path.join(downloadsDir, "map.html")
map.save("map.html")