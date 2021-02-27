import datetime


def get_date():
    """ Return today's date as a string for psql timestamps """
    today = str(datetime.datetime.now())
    today = today.split(".")
    today = today[0]
    return today
