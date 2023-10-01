import json
import pandas as pd
import numpy as np
import folium as fol
import openpyxl
from branca.colormap import LinearColormap

populationDataframe = pd.read_excel('Usable Data.xlsx', sheet_name="CO-EST2022-POP", skiprows=2, usecols="A, C:H", nrows=3100)
populationDataframe.set_index('id', inplace=True)
#print(populationDataframe)
  

m = fol.Map(location=(40, -100),
        control_scale=True, 
        zoom_control=False, 
        zoom_start=6)

with open('us-counties.json', 'r') as countiesJson:
    USCounties = json.load(countiesJson)

colorMap2020 = LinearColormap(colors=['#BFD7EA', '#3F6C7E', '#001D2F', '#90B796', '#005A11', '#FADD7D', '#724F00', '#FFDAB9', '#FF8038', '#C43200', '#FFD1D1', '#FF5959', '#B80000'], 
    index = [0, 10_000, 25_000, 50_000, 100_000, 150_000, 200_000, 500_000, 1_000_000, 2_000_000, 4_000_000, 8_000_000, 10_000_000], 
    vmin=0, vmax=10_000_000, 
    caption='Population'
)

def getColor(value):
    return colorMap2020(value)
    
#County Population in 2020
Choro2020 = fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=1, 
    line_weight=2, 
    data=populationDataframe,
    columns=[populationDataframe.index, '2020 Population'],
    threshold_scale=[0, 10_000, 25_000, 50_000, 100_000, 150_000, 200_000, 500_000, 1_000_000, 2_000_000, 4_000_000, 8_000_000, 10_000_000],
    key_on='feature.id',
    fill_color='YlOrRd', 
    name='2020 Population by County',
)

Choro2020.add_to(m)

#2020-2021 Percent Change
Choro2020_2021 = fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=1, 
    line_weight=2, 
    data=populationDataframe,
    columns=[populationDataframe.index, "2020-2021 Percent Change"],
    threshold_scale=[-13, -10, -7, -4, -3, -2.5, -2, -1.75, -1.5, -1.25, -1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 4, 7, 10, 13],
    key_on='feature.id',
    fill_color='RdYlGn', 
    name='2020-2021 Percent Change'
).add_to(m)


#2021-2022 Percent Change
Choro2021_2022 = fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=1, 
    line_weight=2, 
    data=populationDataframe,
    columns=[populationDataframe.index, "2021-2022 Percent Change"],
    threshold_scale=[-13, -10, -7, -4, -3, -2.5, -2, -1.75, -1.5, -1.25, -1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 4, 7, 10, 13],
    key_on='feature.id',
    fill_color='RdYlGn', 
    name='2021-2022 Percent Change'
).add_to(m)

fol.LayerControl().add_to(m)
m.save("map.html")
