"""
TODO:
"""
import base64
import folium as fol
from folium.plugins import FloatImage

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
            nameColumn (str): The column in the dataFrame to use for labeling.

        Returns:
            None
        """
        
        #handling overflow for non python3
        if dataColumn == "Top 20 KMA Population 2020 (millions)" or dataColumn == "Top 20 KMA Population 2021 (millions)" or dataColumn == "Top 20 KMA Population 2022 (millions)":
            dataFrame[dataColumn] = dataFrame[dataColumn] / 1_000_000
            
        
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
            show=False,
            bins=self.create_bins(name)
        )

        tooltip = self.add_tooltip(layer, dataFrame, dataColumn, nameColumn)
        tooltip.add_to(layer.geojson)
            
        self.m.add_child(layer)
        
        
    def add_empty_layer(self, geodata, name):
        """
        Creates a layer for the map that is not meant to display any data
        and adds it to the map. This is used to create the County Lines and KMA Lines layers.

        Args: 
            geodata (str): The GeoJSON to be plotted in the form of a string
            name (str): The name of the layer
        """

        layer = fol.GeoJson(data=geodata, 
                            name=name, 
                            show=False, 
                            style_function= lambda feature:{
                                "fillColor" : "transparent",
                                "color": "black", 
                                "weight": 1
                            }
                            )
        
        self.m.add_child(layer)
        


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
        try:
            with open(directory + "/data/input/FW_watermark.png", 'rb') as wm:
                b64_content = base64.b64encode(wm.read()).decode('utf-8')
                
            FloatImage('data:image/png;base64,{}'.format(b64_content), bottom=5, left=0, width=100, height=25).add_to(self.m)
        except FileNotFoundError as e:
            print(f"ERROR: The FW_watermark.png was not found. {e}")
        except (PermissionError, IOError) as e:
            print(f"ERROR: Unable to read the file. {e}") 
        except ValueError as e:
            print(f"ERROR: Invalid PNG header. {e}")
        except Exception as e:
            print(f"ERROR: Unexpected error. {e}")

        
        
    def create_bins(self, layer_name):
        """
        Customizes the bins for the color scale of the layer this function is called on.

        Args:
            layer_name (string): The name of the layer

        Return:
            The customized bins for the layer
        """
        
        bins =[]
        
        if layer_name == "Top 20 KMA Population 2020 (millions)" or layer_name == "Top 20 KMA Population 2021 (millions)" or layer_name == "Top 20 KMA Population 2022 (millions)":
            bins = [1, 3, 6, 8, 10, 15]
        elif layer_name == "All KMA 2020-2022 Population Change":
            bins = [-450_000, -300_000, -100_000, 0, 100_000, 200_000, 350_000]
        elif layer_name == "Top 20 KMA Population Percent Change 2020-2022":
            bins = [-4, -3, -1, 0, 1, 3, 5]
        elif layer_name == "Top 20 KMA Population Total Change 2020-2022":
            bins = [-450_000, -300_000, -100_000, 0, 100_000, 200_000, 350_000]
        elif layer_name == "Top 20 KMA Freight Percent Change 2020-2022":
            bins = [-35, -25, -15, -5, 0, 5, 10, 15]
        elif layer_name == "Top 20 KMA Freight Total Change 2020-2022":
            bins = [-30_000, -20_000, -10_000, 0, 5_000, 10_000, 15_000]
        elif layer_name == "All KMA Freight Percent Change 2020-2022":
            bins = [-60, -40, -20, 0, 20, 40, 60]
        
        return bins
    