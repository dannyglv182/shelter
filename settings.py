import psycopg2
import datetime

def connect():
    """Establishes a connection to the database"""
    try:
        conn = psycopg2.connect("dbname = shelter")
        return conn
    except:
        print "Connection failed."
