"""
TODO:
"""
import sqlite3 as sql

class DatabaseManipulator():
    def __init__(self, path):
        
        """
        Initialize a DatabaseManipulator object and connect to a SQLite database.

        Args:
            path (str): The path to the SQLite database file to connect to.
        """
        
        self.con = sql.connect(path)
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