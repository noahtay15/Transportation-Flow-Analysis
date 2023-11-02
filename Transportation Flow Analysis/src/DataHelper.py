"""
TODO:
    - Tuple to JSON
    - Tuple to data frame
"""
import geojson
import pandas as pd

class DataHelper:
    
    def tuple_to_json(self, tup_list):
        """
        Transforms a list of tuples into a json object. Not all elements in the tuples are used
         
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
                
        Returns:
            Technically, geo_data is a string, but it's json
        
        """
        
        features = []
        #id, kma, kma_name, [data], geometry
        for row in tup_list:
            
            if "MULTIPOLYGON" in row[4]:
                geo_type = "MULTIPOLYGON"
                geo_coord = row[4].replace('MULTIPOLYGON', '')
            else:
                geo_type = "POLYGON"
                geo_coord = row[4].replace('POLYGON', '')
                
            geo_coord = geo_coord.replace('(', '[').replace(')', ']')
            geo_coord = "[" + geo_coord + "]"
            
            feature = {
                "type" : "Feature",
                "id": str(row[0]),
                "properties": {"name": row[2]},
                "geometry": {
                    "type": geo_type,
                    "coordinates": geo_coord
                }
            }
            features.append(feature)
            
        feature_collection = {
            "type": "FeatureCollection",
            "features": features
        }
        
        geo_data = geojson.dumps(feature_collection)
        return geo_data
    
    def tuple_to_dataframe(self, tup_list, data_column_name):
        """
        Transforms a list of tuples from the query into the data frame needed to insert into the choropleths.
        Only takes id, kma, kma_name, data, geometry
        
        Args:
            tup_list (list of tuples): The list of tuples from the query
            data_column_name (string): This should be the name of the map layer to keep it simple
        """
        columns =["id", "kma", "kma_name", data_column_name, "geometry"]
        
        selected_data =[]
        for tup in tup_list:
            selected_data.append((tup[0], tup[1], tup[2], tup[3], tup[4]))
        df = pd.DataFrame(selected_data, columns=columns)
        df =df.set_index('id')
        
        return df