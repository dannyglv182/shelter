import psycopg2
import datetime
from settings import connect
from helpers import get_date

def add_dog(name):
    """Add a new dog to the shelter."""
    today = get_date()

    # Add the new dog to the database
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT into dog (name, arrival_date) VALUES (%s, %s)", (name, today))
    conn.commit()
    conn.close()
