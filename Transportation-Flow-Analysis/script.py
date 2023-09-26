import json
import pandas as pd
import numpy as np
import folium as fol
import openpyxl


populationDataframe = pd.read_excel('Usable Data.xlsx', sheet_name="CO-EST2022-POP", skiprows=2, usecols="A, C:H", nrows=3100)
populationDataframe.set_index('id', inplace=True)
print(populationDataframe)


m = fol.Map(location=(40, -100),
        control_scale=True, 
        zoom_control=False, 
        zoom_start=6)

with open('us-counties.json', 'r') as countiesJson:
    USCounties = json.load(countiesJson)


#County Population
fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=1, 
    line_weight=2, 
    data=populationDataframe,
    columns=[populationDataframe.index, '2020 Population'],
    threshold_scale=[0, 10_000, 25_000, 50_000, 100_000, 150_000, 200_000, 500_000, 1_000_000, 2_000_000, 4_000_000, 8_000_000, 10_000_000],
    key_on='feature.id',
    fill_color='YlGnBu', 
    name='2020 Population by County', 
    norm='log'
).add_to(m)

for year in ['2020-2021 Percent Change', '2021-2022 Percent Change']:
    fol.Choropleth(
        geo_data=USCounties, 
        fill_opacity=1, 
        line_weight=2, 
        data=populationDataframe,
        columns=[populationDataframe.index, year],
        threshold_scale=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        key_on='feature.id',
        fill_color='YlGnBu', 
        name=f'{year}', 
        norm='log'
    ).add_to(m)

"""
stateLoadsChloro = fol.Choropleth(
    
).add_to(m)
"""

fol.LayerControl().add_to(m)
m.save("map.html")
