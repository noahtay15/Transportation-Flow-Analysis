"""
TODO:
    - Everything
"""

import folium as fol
import DatabaseManipulator as dbMan

class MapMaker():
    def __init__(self):
        self.map = fol.Map(location=(40, -100),
                            control_scale=True, 
                            zoom_control=False, 
                            zoom_start=5, 
                            min_zoom=5,
                            max_bounds=True,
                            min_lon=-130, 
                            max_lon=-60,
                            min_lat=20,
                            max_lat=52,
                            tiles="Cartodb Positron")

    """
        Add a choropleth layer, with tooltip, to the map with specified data and
        style and adds it to the map object

        Args:
            dataFrame (pandas.DataFrame): The data source for the choropleth layer.
            geodata (str): The GeoJSON data source for the choropleth layer.
            dataColumn (str): The column in the dataFrame to use for coloring the map.
            fillColor (str): The fill color for the choropleth layer.
            name (str): The name of the layer on the map.
            show (bool): Whether to show the layer by default.
            nameColumn (str): The column in the dataFrame to use for labeling.

        Returns:
            None
        """
    def add_layer(self, dataFrame, geodata, dataColumn, fillColor, name, show, nameColumn):
        layer = fol.Choropleth(
            geo_data=geodata, 
            fill_opacity=1, 
            line_weight=0.5, 
            data=dataFrame,
            columns=[dataFrame.index, dataColumn],
            key_on='feature.id',
            fill_color=fillColor, 
            name=name,
            nan_fill_opacity=0, 
            legend_name=name,
            show=show
        )
        
        tooltip = self.add_tooltip(layer, dataFrame, dataColumn, nameColumn)
        tooltip.add_to(layer.geojson)
        layer.add_to(self.map)

    def add_tooltip(self, layer, dataFrame, dataColumn, nameColumn):
        for s in layer.geojson.data['features']:
            feature_id = int(s['id'])  # Convert the GeoJSON id to an integer
            s['properties'][dataColumn] = int(dataFrame.loc[feature_id, dataColumn])
            s['properties'][nameColumn] = str(dataFrame.loc[feature_id, nameColumn])
        
        return fol.GeoJsonTooltip([nameColumn, dataColumn])

    def get_map(self):
        return self.map       
        
    
        
        
