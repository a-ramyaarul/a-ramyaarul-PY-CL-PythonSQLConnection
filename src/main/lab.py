"""
This lab will explore establishing a database connection via Python and SQLite.
"""
import sqlite3


class Lab:

    # TODO: Complete the try block in connect_to_database(), returning a Database Connection object
    def connect_to_database(self):

        try:
            print("Connecting to database...")
            return sqlite3.connect('database.db')
        except Exception as e:
            print(f"Failed to connect to database, with Exception: {e}")
            return None
