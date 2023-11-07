"""
TODO: 
    - all map-making methods
    - figure out how to hide the color scales when the layer is not active
    - edit the geometry column in the KMA table to be the correct format
"""
import os
from DBManipulator import DBManipulator
from MapMaker import MapMaker
from DataHelper import DataHelper

def main():
    #Changing the working directory
    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(script_directory)
    os.chdir(parent_directory)
    current_directory = os.getcwd()
    #print("Current working directory:", current_directory) #/workspaces/Transportation-Flow-Analysis/Transportation Flow Analysis
    
    #accessing database file
    db = DBManipulator(current_directory)

    mapMaker = MapMaker()
    dHelp = DataHelper()


    """Noah, don't worry about the County Lines and KMA Lines map. I think there is something special that 
        has to be done since I am filling in a choropleth with no data. I'll figure it out unless you want
        to attempt it. -Clifton"""
    
    """County Lines"""
    #may have to just create it here instead of trying to fit into add_layer method
    #store tuple from query in variable: result
    #transform id and name from tuple into dataframe: dataFrame
    #add 'data' column to dataFrame, fill with all NONE
    #transform id, name, geometry from tuple into json: geodata
    #pass dataFrame into dataFrame, geodata into geodata, anything into fillColor, "County Lines" into  

    """KMA Lines"""
    #store tuple from query in variable: result
    #transform id and name from tuple into dataframe: dataFrame
    #add 'data' column to dataFrame, fill with all NONE
    #transform id, name, geometry from tuple into json: geodata
    #pass dataFrame into dataFrame, geodata into geodata, anything into fillColor, "" into 

    

    """KMAs 2020 Population"""
    result = db.fetch_KMA_Top20_2020_Population() #store tuple from query in variable: result
    dataFrame = dHelp.tuple_to_dataframe(result, "Top 20 KMA Population 2020") #transform id, kma_name, and the data from tuple into dataframe: dataFrame
    m = mapMaker.get_map()
    geodata = dHelp.tuple_to_json(result) #transform id, kma_name, geometry from tuple into json: geodata
    #pass dataFrame into dataFrame, geodata into geodata, preferred color scheme into fillColor, the layer name into name, "kma_name" into nameColumn, True into isAddToolTip if this is not the County Lines or KMA Lines layer, the same string as name into dataColumn
    mapMaker.add_layer(dataFrame=dataFrame, geodata=geodata, fillColor='YlOrRd', name="Top 20 KMA Population 2020", nameColumn = "kma_name", isAddTooltip=True, dataColumn="Top 20 KMA Population 2020")
    
    """KMAs 2021 Population"""
    result = db.fetch_KMA_Top20_2021_Population() #store tuple from query in variable: result
    dataFrame = dHelp.tuple_to_dataframe(result, "Top 20 KMA Population 2021") #transform id, kma_name, and the data from tuple into dataframe: dataFrame
    m = mapMaker.get_map()
    geodata = dHelp.tuple_to_json(result) #transform id, kma_name, geometry from tuple into json: geodata
    #pass dataFrame into dataFrame, geodata into geodata, preferred color scheme into fillColor, the layer name into name, "kma_name" into nameColumn, True into isAddToolTip if this is not the County Lines or KMA Lines layer, the same string as name into dataColumn
    mapMaker.add_layer(dataFrame=dataFrame, geodata=geodata, fillColor='YlOrRd', name="Top 20 KMA Population 2021", nameColumn = "kma_name", isAddTooltip=True, dataColumn="Top 20 KMA Population 2021")
    
    
    """KMAs 2022 Population"""
    result = db.fetch_KMA_Top20_2022_Population() #store tuple from query in variable: result
    dataFrame = dHelp.tuple_to_dataframe(result, "Top 20 KMA Population 2022") #transform id, kma_name, and the data from tuple into dataframe: dataFrame
    m = mapMaker.get_map()
    geodata = dHelp.tuple_to_json(result) #transform id, kma_name, geometry from tuple into json: geodata
    #pass dataFrame into dataFrame, geodata into geodata, preferred color scheme into fillColor, the layer name into name, "kma_name" into nameColumn, True into isAddToolTip if this is not the County Lines or KMA Lines layer, the same string as name into dataColumn
    mapMaker.add_layer(dataFrame=dataFrame, geodata=geodata, fillColor='YlOrRd', name="Top 20 KMA Population 2022", nameColumn = "kma_name", isAddTooltip=True, dataColumn="Top 20 KMA Population 2022")
    
    
    
    
    
    
    #The next three lines should be the very last thing called in the main method
    m = mapMaker.get_map()
    mapMaker.add_layer_control()
    m.save(current_directory + "/data/map.html")
    
    


    


    


    """
    #Inserting the KMA table
    csv.field_size_limit(sys.maxsize)
    data=[]
    with open(current_directory + "/data/input/geo_kma.csv", 'r', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the first line

        for row in csv_reader:
            # Convert row elements to a tuple and append to the list
            data_tuple = tuple(row)
            data.append(data_tuple)
        
    data = sorted(data, key=lambda x: x[0])    
     
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
            
    modified_list = [(t[2], t[1], t[0], t[3]) for t in data] #id, kma_name, kma, geometry
    
    for row in modified_list: 
        print(row[0] + ' ' + row[1] + ' ' + row[2])

     
    
    #read excel file, fill in the list of tuple with all the data, create table, fill in table  
    
    dataFrame = pd.read_excel(current_directory + "/data/input/KMA_and_County_Data_FINAL_Rev2.xlsx", sheet_name="Combined KMA", usecols="A:S")
    elem = [t[1] for t in modified_list]
    new_col = pd.DataFrame({'kma': elem})
    dataFrame = pd.concat([dataFrame.iloc[:, :2], new_col, dataFrame.iloc[:, 2:]], axis=1)
    elem = [t[3] for t in modified_list]
    dataFrame['geometry'] = elem
    dataFrame = dataFrame.sort_values(by='id', ascending=True)
    print(dataFrame)
    print(dataFrame.info())
    #db.execute_command("")

    fullKMAData = [] #the list of tuple to be put into the KMA table
    for index, row in dataFrame.iterrows():
        processed_row = []
        for column_name, value in row.items():
            if column_name == 'id' or column_name == 'Sum of 2020 Population' or column_name == 'Sum of 2021 Population' or column_name == 'Sum of 2022 Population' or column_name == 'KMA Population Change 2020-2021' or column_name == 'KMA Population Change 2021-2022' or column_name == 'KMA Population Change 2020-2022' or column_name == 'Population Absolute Value Change 2020-2022' or column_name == 'KMA Freight Change 2020-2021' or column_name == 'KMA Freight Change 2021-2022' or column_name == 'KMA Freight Change 2020-2022' or column_name == 'Freight Absolute Value Change 2020-2022':
                processed_row.append(int(value))
            elif column_name == 'kma_name' or column_name == 'kma' or column_name == 'geometry':
                processed_row.append(str(value))
            elif column_name == 'KMA Population Percent Change 2020-2021' or column_name == "KMA Population Percent  Change 2021-2022" or column_name == 'KMA Population Percent Change 2020-2022' or column_name == 'KMA Freight Percent Change 2020-2021' or column_name == 'KMA Freight Percent Change 2021-2022' or column_name == 'KMA Freight Percent Change 2020-2022':
                processed_row.append(float(value))
            
        fullKMAData.append(tuple(processed_row))

    for t in fullKMAData:
        tupNoGeo = t[:-1]
        print(*tupNoGeo)

    
    db.execute_command("DROP TABLE IF EXISTS KMAs")
    
    db.execute_command('''CREATE TABLE KMAs (
                       id INTEGER PRIMARY KEY, 
                       kma TEXT, 
                       kma_name TEXT, 
                       population_2020 INTEGER, 
                       population_2021 INTEGER, 
                       population_2022 INTEGER, 
                       Pop_Chan_2020_2021 INTEGER, 
                       Pop_Perc_Chan_2020_2021 REAL,
                       Pop_Chan_2021_2022 INTEGER,
                       Pop_Perc_Chan_2021_2022 REAL,
                       Pop_Chan_2020_2022 INTEGER,
                       Pop_Perc_Chan_2020_2022 REAL,
                       Pop_Abs_Val_Chan_2020_2022 INTEGER,
                       Fre_Chan_2020_2021 INTEGER,
                       Fre_Perc_Chan_2020_2021 REAL,
                       Fre_Chan_2021_2022 INTEGER,
                       Fre_Perc_Chan_2021_2022 REAL,
                       Fre_Chan_2020_2022 INTEGER,
                       Fre_Perc_Chan_2020_2022 REAL,
                       Fre_Abs_Val_Chan_2020_2022 INTEGER,
                       geometry TEXT
                       )''')
    
    
    db.fill_table('''INSERT INTO KMAs (
                  id, 
                  kma, 
                  kma_name, 
                  population_2020, 
                  population_2021, 
                  population_2022, 
                  Pop_Chan_2020_2021, 
                  Pop_Perc_Chan_2020_2021, 
                  Pop_Chan_2021_2022, 
                  Pop_Perc_Chan_2021_2022, 
                  Pop_Chan_2020_2022,
                  Pop_Perc_Chan_2020_2022, 
                  Pop_Abs_Val_Chan_2020_2022, 
                  Fre_Chan_2020_2021,
                  Fre_Perc_Chan_2020_2021, 
                  Fre_Chan_2021_2022, 
                  Fre_Perc_Chan_2021_2022, 
                  Fre_Chan_2020_2022,
                  Fre_Perc_Chan_2020_2022, 
                  Fre_Abs_Val_Chan_2020_2022, 
                  geometry)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                 ''', fullKMAData)
    

    print(db.fetch_data('SELECT id, kma, kma_name, Fre_Chan_2020_2022 FROM KMAs'))
    """

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
    

main()