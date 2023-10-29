"""
TODO: 
    - EVERYTHING
"""
import os
import json
import csv
import sys
from DBManipulator import DBManipulator

def main():
    #Changing the working directory
    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(script_directory)
    os.chdir(parent_directory)
    current_directory = os.getcwd()
    #print("Current working directory:", current_directory) #/workspaces/Transportation-Flow-Analysis/Transportation Flow Analysis
    
    databaseFile = current_directory + "/data/input/database.db"
    db = DBManipulator(databaseFile)
    
    csv.field_size_limit(sys.maxsize)
    
    data=[]
    with open(current_directory + "/data/input/geo_kma.csv", 'r', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the first line

        for row in csv_reader:
            # Convert row elements to a tuple and append to the list
            data_tuple = tuple(row)
            data.append(data_tuple)
     
           
    third_element_dict = {}

    # Loop through the list of tuples
    for data_tuple in data:
        # Get the third element of the current tuple
        third_element = data_tuple[2]
        #print(third_element)
        # Check if the third element is already in the dictionary
        if third_element in third_element_dict:
            # If a duplicate is found, print both tuples
            print("Duplicate Third Element:", third_element)
            print("Tuple 1:", third_element_dict[third_element])
            print("Tuple 2:", data_tuple)
        else:
            # If it's not a duplicate, add it to the dictionary with the associated tuple
            third_element_dict[third_element] = data_tuple
            
    modified_list = [(t[2], t[1], t[0]) for t in data] #id, kma_name, kma, geometry
    
    for row in modified_list: 
        print(row[0] + ' ' + row[1] + ' ' + row[2])
        
    fullKMAData = [] #the list of tuple to be put into the KMA table
    #read excel file, fill in the list of tuple with all the data, create table, fill in table  
        
    #db.execute_command("")
    
    
    """
    Filling counties table
    with open(current_directory + "/data/input/us-counties.json", "r") as file:
        data = json.load(file)
        
    tableData = []
    for feature in data["features"]:
        feature_id = feature["id"]
        feature_name = feature["properties"]["name"]
        feature_geometry = json.dumps(feature["geometry"])
        tableData.append((feature_id, feature_name, feature_geometry))
        
    print(tableData)
    db.fill_table("INSERT INTO counties (id, name, geometry) VALUES (?, ?, ?)", tableData)
    print(db.fetch_data("SELECT * FROM counties"))
    """
    db.close_con()

main()