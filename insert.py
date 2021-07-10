import psycopg2
import datetime
from settings import connect
from helpers import get_date


def add_dog(name):
    """Add a new dog to the dog table."""
    today = get_date()

    # Add the new dog to the database
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT into dog (name, arrival_date) VALUES (%s, %s)", (name, today))
    conn.commit()
    conn.close()


def add_food(name, wet):
    """Add a new food to the food table."""
    if wet == "2":
        wet = "true"
    else:
        wet = "false"

    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT into food (name, wet) VALUES (%s, %s)", (name, wet))
    conn.commit()
    conn.close()


def add_adopter(first_name, last_name, email):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT into adopter (first_name, last_name, email) VALUES (%s, %s, %s)", (first_name, last_name, email))
    conn.commit()
    conn.close()


def add_adoption(adopter_id, dog_id):
    """ Add a new adoption record """
    today = get_date()
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO adopter_dog (adopter_id, dog_id, adoption_date) VALUES (%s, %s, %s)", (adopter_id, dog_id, today))
    conn.commit()
    conn.close()


