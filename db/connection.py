import sqlite3
from sqlite3 import Error

def create_connection():

    try:
        conn = sqlite3.connect('db/db_consultora.sqlite3')
        return conn
    except Error as e:
        print("Error connecting to db: " + str(e))