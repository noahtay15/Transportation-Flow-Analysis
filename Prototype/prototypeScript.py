import json
import pandas as pd
import folium as fol

populationDataframe = pd.read_excel('/workspaces/Transportation-Flow-Analysis/Prototype/Usable Data.xlsx', sheet_name="CO-EST2022-POP", skiprows=2, usecols="A, C:L", nrows=3100)
populationDataframe.set_index('id', inplace=True)
#print(populationDataframe)

#filter dataframe by top 20 of 2020 county population
filterTop20DF= populationDataframe.sort_values(by='2020 Population', ascending = False)
filterTop20DF = filterTop20DF.head(20)
#print(filterTop20DF)


m = fol.Map(location=(40, -100),
        control_scale=True, 
        zoom_control=False, 
        zoom_start=6,
        tiles= "Cartodb Positron")

with open('/workspaces/Transportation-Flow-Analysis/Prototype/us-counties.json', 'r') as countiesJson:
    USCounties = json.load(countiesJson)

    
#County Population in 2020
Choro2020Pop = fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=1, 
    line_weight=0, 
    data=filterTop20DF,
    columns=[filterTop20DF.index, '2020 Population'],
    key_on='feature.id',
    fill_color='YlOrRd', 
    name='2020 Population by County',
    nan_fill_opacity=0, 
    legend_name="2020 Population by County",
    show=True
).add_to(m)


#2020-2021 Percent Change
Choro2020_2021Perc = fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=1, 
    line_weight=2, 
    data=filterTop20DF,
    columns=[filterTop20DF.index, "2020-2021 Percent Change"],
    key_on='feature.id',
    fill_color='RdYlGn', 
    name='2020-2021 Percent Change',
    nan_fill_opacity=0, 
    legend_name="2020-2021 Percent Change",
    show=False
).add_to(m)


#2021-2022 Percent Change
Choro2021_2022Perc = fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=1, 
    line_weight=2, 
    data=filterTop20DF,
    columns=[filterTop20DF.index, "2021-2022 Percent Change"],
    key_on='feature.id',
    fill_color='RdYlGn', 
    name='2021-2022 Percent Change',
    nan_fill_opacity=0,
    legend_name="2021-2022 Percent Change",
    show=False
).add_to(m)


#2020-2022 Percent Change
Choro2021_2022Perc = fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=1, 
    line_weight=2, 
    data=filterTop20DF,
    columns=[filterTop20DF.index, "2020-2022 Percent Change"],
    key_on='feature.id',
    fill_color='RdYlGn', 
    name='2020-2022 Percent Change',
    nan_fill_opacity=0,
    legend_name="2020-2021 Percent Change",
    show=False
).add_to(m)

#2020-2021 Raw Change
Choro2020_2021Raw = fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=1, 
    line_weight=2, 
    data=filterTop20DF,
    columns=[filterTop20DF.index, "2020-2021 Raw Change"],
    key_on='feature.id',
    fill_color='RdYlGn', 
    name='2020-2021 Raw Change',
    nan_fill_opacity=0,
    legend_name="2020-2021 Raw Change",
    show=False
).add_to(m)

#2021-2022 Raw Change
Choro2021_2022Raw = fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=1, 
    line_weight=2, 
    data=filterTop20DF,
    columns=[filterTop20DF.index, "2021-2022 Raw Change"],
    key_on='feature.id',
    fill_color='RdYlGn', 
    name='2021-2022 Raw Change',
    nan_fill_opacity=0,
    legend_name="2021-2022 Raw Change",
    show=False
).add_to(m)

#2020-2022 Raw Change
Choro2020_2022Raw = fol.Choropleth(
    geo_data=USCounties, 
    fill_opacity=1, 
    line_weight=2, 
    data=filterTop20DF,
    columns=[filterTop20DF.index, "2020-2022 Raw Change"],
    key_on='feature.id',
    fill_color='RdYlGn', 
    name='2020-2022 Raw Change',
    nan_fill_opacity=0,
    legend_name="2020-2022 Raw Change",
    show=False
).add_to(m)


fol.LayerControl().add_to(m)

m.save("/workspaces/Transportation-Flow-Analysis/Prototype/map.html")
