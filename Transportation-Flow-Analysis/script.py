import json
import pandas as pd
import folium as fol
import openpyxl


populationDataframe = pd.read_excel('Somewhat Fixed 2.xlsx', sheet_name="CO-EST2022-POP", skiprows=2, usecols="C:F", nrows=3100)
populationDataframe.set_index('id', inplace=True)
print(populationDataframe)


m = fol.Map(location=(40, -100),
        control_scale=True, 
        zoom_control=False, 
        zoom_start=6)

with open('us-counties.json', 'r') as countiesJson:
    USCounties = json.load(countiesJson)


#County Population
for year in ['2020 Population', '2021 Population', '2022 Population']:
    fol.Choropleth(
        geo_data=USCounties, 
        fill_opacity=1, 
        line_weight=2, 
        data=populationDataframe,
        columns=[populationDataframe.index, year],
        threshold_scale=[0, 50000, 100000, 150000, 200000, 10000000],
        key_on='feature.id',
        fill_color='YlGnBu', 
        name=f'{year} by County'
    ).add_to(m)


"""
stateLoadsChloro = fol.Choropleth(
    
).add_to(m)
"""

fol.LayerControl().add_to(m)
m.save("map.html")
