import json
import pandas as pd
import folium as fol

populationDataframe = pd.read_csv('/workspaces/Transportation-Flow-Analysis/Prototype/Usable Data.csv')
#print(populationDataframe.info())
    
populationDataframe.set_index('id', inplace=True)
#print(populationDataframe)

#filter dataframe by top 20 of 2020 county population
filterTop20DF= populationDataframe.sort_values(by='2020 Population', ascending = False)
filterTop20DF = filterTop20DF.head(20)
#print(filterTop20DF)
max_lat = 52
min_lat = 20
max_lon = -60
min_lon = -130

m = fol.Map(location=(40, -100),
        control_scale=True, 
        zoom_control=False, 
        zoom_start=5, 
        min_zoom=5,
        max_bounds=True,
        min_lon=min_lon, 
        max_lon=max_lon,
        min_lat=min_lat,
        max_lat=max_lat,
        tiles= "Cartodb Positron")

fol.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(m)
fol.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(m)
fol.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(m)
fol.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(m)

with open('/workspaces/Transportation-Flow-Analysis/Prototype/us-counties.json', 'r') as countiesJson:
    USCounties = json.load(countiesJson)
countiesJson.close()


"""The next lines all the way to Choro2020PopTop20.add_to(m) are how
    to add tooltips to choropleths"""

with open('/workspaces/Transportation-Flow-Analysis/Prototype/top20us-counties.json', 'r') as top20countiesJson:
    Top20USCounties = json.load(top20countiesJson)
top20countiesJson.close()

#County Population in 2020 of top 20 counties
Choro2020PopTop20 = fol.Choropleth(
    geo_data=Top20USCounties, 
    fill_opacity=1, 
    line_weight=0.5, 
    data=filterTop20DF,
    columns=[filterTop20DF.index, '2020 Population'],
    key_on='feature.id',
    fill_color='YlOrRd', 
    name='2020 Population by County',
    nan_fill_opacity=0, 
    legend_name="2020 Population by County top 20",
    show=True
).add_to(m)

for s in Choro2020PopTop20.geojson.data['features']:
    #print(s)
    feature_id = int(s['id'])  # Convert the GeoJSON id to an integer
    s['properties']['2020 Population'] = int(filterTop20DF.loc[feature_id, '2020 Population'])
    s['properties']['County Name'] = str(filterTop20DF.loc[feature_id, 'County Name'])


fol.GeoJsonTooltip(['County Name', '2020 Population']).add_to(Choro2020PopTop20.geojson)
Choro2020PopTop20.add_to(m)


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
