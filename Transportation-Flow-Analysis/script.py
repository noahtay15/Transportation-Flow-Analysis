import json
import pandas as pd
import folium as fol


m = fol.Map(location=(40, -100),
        control_scale=True, 
        zoom_control=False, 
        zoom_start=6)

with open('us-counties.json', 'r') as countiesJson:
    USCounties = json.load(countiesJson)

countyPopChloro = fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=0.3, 
    line_weight=2, 
    data=None, #change later
    columns=['id', 'name'],
    key_on='feature.id',
    fill_color='YlGnBu', 
    name='Population by County'
).add_to(m)

""" Add later
stateLoadsChloro = fol.Choropleth(
    
).add_to(m)
"""

fol.LayerControl().add_to(m)
m.save("map.html")