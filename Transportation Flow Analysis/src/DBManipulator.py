"""
TODO:
    - Restructure for better encapsulation
        * Change fetch_data() into multiple fetching methods for diff types of data. Have SQL commands inside those methods
"""
import sqlite3 as sql

class DBManipulator():
    def __init__(self, directory):
        
        """
        Initialize a DatabaseManipulator object and connect to a SQLite database.

        Args:
            path (str): The path to the SQLite database file to connect to.
        """
        
        self.con = sql.connect(directory + "/data/input/database.db")
        self.cur = self.con.cursor()
        
    def execute_command(self, command):
        
        """
        Execute an SQL command and commit the changes to the database.

        Args:
            command (str): The SQL command to be executed.
        """
        
        self.cur.execute(command)
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
    
    def fetch_counties(self):
        """
        Fetches the results of an SQL query to get the id, name, and geometry of the counties

        Returns:
            list of tuples: A list of tuples containing the id number, name, and geojson geometry
                of the counties
        """
        res = self.cur.execute("SELECT * FROM counties")
        return res.fetchall()

    def fetch_KMA_Pop2020(self):
        

    def fill_table(self, command, data):
        
        """
        Execute an SQL command to insert multiple rows of data into a table.

        Args:
            command (str): The SQL command to insert data into the table.
            data (list of tuples): Data to be inserted into the table.
        """
        
        self.cur.executemany(command, data)
        self.con.commit()
        
    def close_con(self):
        
        """
        Closes the database connection
        """
        self.con.close()