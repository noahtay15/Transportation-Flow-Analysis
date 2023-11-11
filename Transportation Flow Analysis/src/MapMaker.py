"""
TODO:
"""

import folium as fol
from folium.plugins import FloatImage
import base64

class MapMaker():
    def __init__(self):
        
        """
        Initialize a MapMaker object with default map settings.

        This constructor sets up a Folium map with default parameters, including a specified
        location, zoom level, map boundaries, and tileset. It provides a starting point for
        further customization and adding layers to the map.

        Attributes:
            map (folium.Map): The Folium map object.

        Default Parameters:
            - Location: Latitude 40, Longitude -100
            - Map Controls: Scale control enabled, zoom control disabled
            - Zoom Level: 5
            - Minimum Zoom Level: 5
            - Maximum Bounds: Set to a region within longitude -130 to -60 and latitude 20 to 52.
            - Tiles: "Cartodb Positron" tileset
        """
        
        self.m = fol.Map(location=(40, -100), 
                            zoom_control=False, 
                            zoom_start=5, 
                            min_zoom=5,
                            max_bounds=True,
                            min_lon=-130, 
                            max_lon=-60,
                            min_lat=20,
                            max_lat=52,
                            tiles="Cartodb Positron")
        

    def add_layer(self, dataFrame, geodata, fillColor, name, nameColumn, dataColumn):
        
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
        
        layer = fol.Choropleth(
            geo_data=geodata, 
            fill_opacity=0.7, 
            line_weight=1,
            line_opacity=1, 
            data=dataFrame,
            columns=[dataFrame.index, dataColumn],
            key_on='feature.id',
            fill_color=fillColor, 
            name=name,
            nan_fill_opacity=0, 
            legend_name=name,
            show=False
        )

        tooltip = self.add_tooltip(layer, dataFrame, dataColumn, nameColumn)
        tooltip.add_to(layer.geojson)
            
        self.m.add_child(layer)
        
        
    def add_empty_layer(self, geodata, name):
        layer = fol.Choropleth(
            geo_data=geodata, 
            fill_opacity=0.7, 
            line_weight=1,
            line_opacity=1,
            key_on='feature.id',
            name=name,
            nan_fill_opacity=0, 
            legend_name=name,
            show=False
        )
        


    def add_tooltip(self, layer, dataFrame, dataColumn, nameColumn):
        
        """
        A helper method for adding tooltips to a choropleth layer for displaying additional information.

        Args:
            layer (folium.Choropleth): The choropleth layer to which tooltips will be added.
            dataFrame (pandas.DataFrame): The data source for tooltip information.
            dataColumn (str): The column in the dataFrame used for data display in the tooltip.
            nameColumn (str): The column in the dataFrame used for feature names in the tooltip.

        Returns:
            folium.GeoJsonTooltip: The tooltip configuration added to the choropleth layer.
        """
        
        for s in layer.geojson.data['features']:
            feature_id = int(s['id'])  # Convert the GeoJSON id to an integer
            s['properties'][dataColumn] = float(dataFrame.loc[feature_id, dataColumn])
            s['properties'][nameColumn] = str(dataFrame.loc[feature_id, nameColumn])
        
        return fol.GeoJsonTooltip([nameColumn, dataColumn])

    def get_map(self):
        
        """
        returns self.map
        """
        
        return self.m      

    def add_layer_control(self):
        """
        Adds layer controls to the map. This should be done after
        all the layers have been added to the map, or the layers
        may not show up correctly on the toggle tool.
        """
        layer_control = fol.LayerControl()
        layer_control.add_to(self.m)
        
        
    def add_watermark(self, directory): 
        """
        Adds the FreightWaves watermark to the map in the bottom left corner. Since it is a png, 
        it must first be base64 encoded into a string.
        
        Args:
            directory (string): the path of the current working directory
        """
        
        with open(directory + "/data/input/FW_watermark.png", 'rb') as wm:
            b64_content = base64.b64encode(wm.read()).decode('utf-8')
            
        FloatImage('data:image/png;base64,{}'.format(b64_content), bottom=5, left=0, width=100, height=25).add_to(self.m)