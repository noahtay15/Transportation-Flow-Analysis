"""
TODO:
"""
import json
import pandas as pd

class DataHelper:
    
    def tuple_to_json(self, tup_list, isEmpty, isKMA):
        """
        Transforms a list of tuples into a json object. Not all elements in the tuples are used.
        The helper function called depends on the isEmpty and isKMA. 
         
        The json object looks like this: 
        {"type":"FeatureCollection","features":[
            ...
            ...
            ...
            {
                "type": "Feature",
                "id": "202",
                "properties": {
                    "name": "Columbia"
                },
                "geometry": {
                    "type": "POLYGON",
                    "coordinates": [all the coordinates data]
                }
            },
            ...
            ...
            ...
        ]}
        Reference top20us-counties.json in Prototype for a better look
        
        Args:
            tup_list (list of tuples): A list of tuples. 
                Index 0 should be id, 
                1: kma,
                2: kma_name,
                3: the data for that layer,
                4: geometry coordinates
            isEmpty (boolean): If tup_list is meant for a layer that will not hold data. True if so
            isKMA (boolean): If tup_list is meant for a KMA or county layer. True if for KMA
                
        Returns:
            A Python object containing deserialized JSON
        
        """
        
        
        #id, kma, kma_name, [data], geometry
        if not isEmpty and isKMA: #if it is a KMA layer with data
            features = self.tup_to_json_KMA(tup_list)
        elif not isKMA and isEmpty: #if it is a county layer without data
            features = self.tup_to_json_county(tup_list)
        elif isEmpty and isKMA: #if it is a KMA layer without data
            features = self.tup_to_json_empty_KMA(tup_list)
            
        feature_collection = {
            "type": "FeatureCollection",
            "features": features
        }
        
        geo_data = json.dumps(feature_collection)
        parsed_geodata = json.loads(geo_data)
        return parsed_geodata
    
    def tuple_to_dataframe(self, tup_list, data_column_name):
        """
        Transforms a list of tuples from the query into the data frame needed to insert into the choropleths.
        Assumes tup_list is a list of tuple in the format (id, kma, kma_name, data, geometry)
        
        Args:
            tup_list (list of tuples): The list of tuples from the query
            data_column_name (string): This should be the name of the map layer to keep it simple
        """
        columns =["id", "kma", "kma_name", data_column_name, "geometry"]
        
        selected_data =[]
        for tup in tup_list:
            selected_data.append((tup[0], tup[1], tup[2], tup[3], tup[4]))

            
        df = pd.DataFrame(selected_data, columns=columns)
        
        df['geometry'] = df['geometry'].str.replace('(', '[')
        df['geometry'] = df['geometry'].str.replace(')', ']')
        df['geometry'] = df['geometry'].str.replace(', ', '],[')
        df['geometry'] = df['geometry'].str.replace(' ', ', ')
        df =df.set_index('id')
        
        return df
    
    def tup_to_json_county(self, tup_list):
        """
        Helper for tup_to_json(). This method makes the features part of the 
        feature collection for the county layer.

        Args:
            tup_list (list of tuples): The list of tuples of the data that goes in each feature

        Returns:
            A list of dictionaries, meant for the county layer 
        """

        features =[]
        for row in tup_list:
            if "MultiPolygon" in row[2]:
                geo_coord = row[2].replace('{"type": "MultiPolygon", "coordinates": ', '').replace("}", "")
                geo_type = "MultiPolygon"
            else:
                geo_coord = row[2].replace('{"type": "Polygon", "coordinates": ', '').replace("}", "")
                geo_type = "Polygon"
            #print(geo_coord)
            geo_coord = json.loads(geo_coord)
            feature = {
                "type" : "Feature",
                "id": int(row[0]),
                "properties": {
                    "name": row[1]},
                "geometry": {
                    "type": geo_type,
                    "coordinates": geo_coord
                }
            }
            #print(feature)
            features.append(feature)

        return features
    
    def tup_to_json_empty_KMA(self, tup_list):
        """
        Helper for tup_to_json(). This method makes the features part of the 
        feature collection for the empty KMA layer.

        Args:
            tup_list (list of tuples): The list of tuples of the data that goes in each feature

        Returns:
            A list of dictionaries, meant for the empty KMA layer
        """

        features = []

        for row in tup_list:  
            if "MULTIPOLYGON" in row[2]:
                geo_type = "MultiPolygon"
                geo_coord = row[2].replace('MULTIPOLYGON', '')
                geo_coord = geo_coord.replace('(', '[').replace(')', ']').replace(', ', '],[').replace(' ', ',').replace('[[[', '[[').replace(']]]', ']]')
                geo_coord = "[[" + geo_coord + "]]"
            else:
                geo_type = "Polygon"
                geo_coord = row[2].replace('POLYGON', '')
                geo_coord = geo_coord.replace('(', '[').replace(')', ']').replace(', ', '],[').replace(' ', ',').replace('[[[', '[[').replace(']]]', ']]')
                geo_coord = "[" + geo_coord + "]"
                    
            geo_coord = json.loads(geo_coord)
            feature = {
                "type" : "Feature",
                "id": int(row[0]), 
                "properties": {
                    "kma_name": str(row[1])},
                "geometry": {
                    "type": geo_type,
                    "coordinates": geo_coord
                }
            }
            features.append(feature)

        return features
    
    def tup_to_json_KMA(self, tup_list):
        """
        Helper for tup_to_json(). This method makes the features part of the 
        feature collection for the KMA layers with data.

        Args:
            tup_list (list of tuples): The list of tuples of the data that goes in each feature

        Returns:
            A list of dictionaries, meant for the KMA layers with data
        """

        features = []

        for row in tup_list:     
            if "MULTIPOLYGON" in row[4]:
                geo_type = "MultiPolygon"
                geo_coord = row[4].replace('MULTIPOLYGON', '')
                geo_coord = geo_coord.replace('(', '[').replace(')', ']').replace(', ', '],[').replace(' ', ',').replace('[[[', '[[').replace(']]]', ']]')                    
                geo_coord = "[[" + geo_coord + "]]"
            else:
                geo_type = "Polygon"
                geo_coord = row[4].replace('POLYGON', '')
                geo_coord = geo_coord.replace('(', '[').replace(')', ']').replace(', ', '],[').replace(' ', ',').replace('[[[', '[[').replace(']]]', ']]')
                geo_coord = "[" + geo_coord + "]"
                    
            geo_coord = json.loads(geo_coord)
            feature = {
                "type" : "Feature",
                "id": int(row[0]),
                "properties": {
                    "kma": str(row[1]),
                    "kma_name": str(row[2]),
                        "data_column_name" : int(row[3])},
                "geometry": {
                    "type": geo_type,
                    "coordinates": geo_coord
                }
            }
            features.append(feature)

        return features