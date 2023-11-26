"""
TODO:
"""
import os
import sqlite3 as sql

class DBManipulator():
    def __init__(self, directory):
        
        """
        Initialize a DatabaseManipulator object and connect to a SQLite database.

        Args:
            directory (str): The working directory path
        """
        if os.path.exists(directory + "/data/input/database.db"):
            self.con = sql.connect(directory + "/data/input/database.db")
            self.cur = self.con.cursor()
        else:
            raise FileNotFoundError("ERROR: The database file was not found. Make sure you have the database file in data\input.")
            
        
    def execute_command(self, command):
        
        """
        Execute an SQL command and commit the changes to the database.

        Args:
            command (str): The SQL command to be executed.
        """
        
        self.cur.execute(command)
        self.con.commit()
    
    def fetch_county_lines(self):
        """
        Fetches the results of an SQL query to get the id, name, and geometry of the counties

        Returns:
            list of tuples: A list of tuples containing the id number, name, and geojson geometry
                of the counties
        """
        res = self.cur.execute("SELECT * FROM counties")
        return res.fetchall()

    def fetch_KMA_lines(self):
        """
        Fetches the id, kma_name, and geometry for the KMAs

        Returns: 
            list of tuples: A list of tuples containing the id, kma, kma_name, and geometry
        """
        res = self.cur.execute("SELECT id, kma_name, geometry FROM KMAs")
        return res.fetchall()
        
    def fetch_KMAs_Pop_Chan_2020_2022(self):
        """
        """
        
        res=self.cur.execute("SELECT id, kma, kma_name, Pop_Chan_2020_2022, geometry FROM KMAs")
        return res.fetchall()

    def fetch_KMA_Top20(self):
        """
        Fetches the id, kma, kma_name, and geometry for the top 20 KMAs
            by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, and geometry
        """
        res = self.cur.execute('''SELECT id, kma, kma_name, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()
    
    def fetch_KMA_Top20_2020_Population(self):
        """
        Fetches the id, kma, kma_name, 2020 population, and geometry 
            for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, population_2020, and geometry
        """
        res = self.cur.execute('''SELECT id, kma, kma_name, population_2020, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()
    
    def fetch_KMA_Top20_2021_Population(self):
        """
        Fetches the id, kma, kma_name, 2021 population, and geometry 
            for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, population_2021, and geometry
        """
        res = self.cur.execute('''SELECT id, kma, kma_name, population_2021, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()
    
    def fetch_KMA_Top20_2022_Population(self):
        """
        Fetches the id, kma, kma_name, 2022 population, and geometry 
            for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, population_2022, and geometry
        """
        res = self.cur.execute('''SELECT id, kma, kma_name, population_2022, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()
    
    def fetch_KMA_Top20_Pop_Per_Chan_2020_2022(self):
        """
        Fetches the id, kma, kma_name, population percent change from 2020-2022, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Pop_Perc_Chan_2020_2022, and geometry
        """
        res = self.cur.execute('''SELECT id, kma, kma_name, Pop_Perc_Chan_2020_2022, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()

    def fetch_KMA_Top20_Pop_Chan_2020_2022(self):
        """
        Fetches the id, kma, kma_name, population change from 2020-2022, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Pop_Chan_2020_2022, and geometry
        """
        res = self.cur.execute('''SELECT id, kma, kma_name, Pop_Chan_2020_2022, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()

    def fetch_KMA_Fre_Perc_Chan_2020_2022(self):
        """
        Fetches the id, kma, kma_name, freight percent change from 2020-2022, 
            and geometry for all the KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Fre_Perc_Chan_2020_2022, and geometry
        """ 
        res = self.cur.execute('''SELECT id, kma, kma_name, Fre_Perc_Chan_2020_2022, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC ''')
        return res.fetchall()

    def fetch_KMA_Top20_Fre_Perc_Chan_2020_2022(self):
        """
        Fetches the id, kma, kma_name, freight percent change from 2020-2022, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Fre_Perc_Chan_2020_2022, and geometry
        """ 
        res = self.cur.execute('''SELECT id, kma, kma_name, Fre_Perc_Chan_2020_2022, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()
    
    def fetch_KMA_Top20_Fre_Chan_2020_2022(self):
        """
        Fetches the id, kma, kma_name, freight change from 2020-2022, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Fre_Chan_2020_2022, and geometry
        """ 
        res = self.cur.execute('''SELECT id, kma, kma_name, Fre_Chan_2020_2022, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()

    def fill_table(self, command, data):
        """
        Execute an SQL command to insert multiple rows of data into a table.

        Args:
            command (str): The SQL command to insert data into the table.
            data (list of tuples): Data to be inserted into the table.
        """
        
        self.cur.executemany(command, data)
        self.con.commit()

    def fetch_data(self, command):
        
        """
        Execute an SQL query and fetch the resulting data.

        Args:
            command (str): The SQL query to be executed.

        Returns:
            list of tuples: A list containing the retrieved data as tuples.
        """
        
        res = self.cur.execute(command)
        return res.fetchall()

    def close_con(self):
        
        """
        Closes the database connection
        """
        self.con.close()











"""HERE ON ARE EXTRA METHODS FOR EXTRACTING DATA / TESTING THE DATABASE

    def fetch_KMA_Top20_Pop_Perc_Chan_2020_2021(self):
        
        Fetches the id, kma, kma_name, population percent change from 2020-2021, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Pop_Perc_Chan_2020_2021, and geometry
        
        res = self.cur.execute('''SELECT id, kma, kma_name, Pop_Perc_Chan_2020_2021, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()

    def fetch_KMA_Top20_Pop_Per_Chan_2021_2022(self):
        
        Fetches the id, kma, kma_name, population percent change from 2021-2022, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Pop_Perc_Chan_2021_2022, and geometry
        
        res = self.cur.execute('''SELECT id, kma, kma_name, Pop_Perc_Chan_2021_2022, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()
    
    def fetch_KMA_Top20_Pop_Chan_2020_2021(self):
        
        Fetches the id, kma, kma_name, population change from 2020-2021, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Pop_Chan_2020_2021, and geometry
        
        res = self.cur.execute('''SELECT id, kma, kma_name, Pop_Chan_2020_2021, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''') 
        return res.fetchall()

    def fetch_KMA_Top20_Pop_Chan_2021_2022(self):
        
        Fetches the id, kma, kma_name, population change from 2021-2022, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Pop_Chan_2021_2022, and geometry
        
        res = self.cur.execute('''SELECT id, kma, kma_name, Pop_Chan_2021_2022, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()
    
    def fetch_KMA_Top20_Fre_Perc_Chan_2020_2021(self):
        
        Fetches the id, kma, kma_name, freight percent change from 2020-2021, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Fre_Perc_Chan_2020_2021, and geometry
        
        res = self.cur.execute('''SELECT id, kma, kma_name, Fre_Perc_Chan_2020_2021, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()

    def fetch_KMA_Top20_Fre_Perc_Chan_2021_2022(self):
        
        Fetches the id, kma, kma_name, freight percent change from 2021-2022, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Fre_Perc_Chan_2021_2022, and geometry
        
        res = self.cur.execute('''SELECT id, kma, kma_name, Fre_Perc_Chan_2021_2022, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()
    
    def fetch_KMA_Top20_Fre_Chan_2020_2021(self):
        
        Fetches the id, kma, kma_name, freight change from 2020-2021, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Fre_Chan_2020_2021, and geometry
         
        res = self.cur.execute('''SELECT id, kma, kma_name, Fre_Chan_2020_2021, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()
    
    def fetch_KMA_Top20_Fre_Chan_2021_2022(self):
        
        Fetches the id, kma, kma_name, freight change from 2021-2022, 
            and geometry for the top 20 KMAs, sorted by Absolute Value Change in Population from 2020-2022
        
        Returns: 
            list of tuples: A list of tuples of the top 20 KMAs, containing
              the id, kma, kma_name, Fre_Chan_2021_2022, and geometry
         
        res = self.cur.execute('''SELECT id, kma, kma_name, Fre_Chan_2021_2022, geometry FROM KMAs
                               ORDER BY Pop_Abs_Val_Chan_2020_2022 DESC 
                               LIMIT 20''')
        return res.fetchall()

    """