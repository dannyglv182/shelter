from insert import *

def test_1():
    """ Add a dog to the database """
    name = "Snoopy"
    add_dog(name);
    return True


test_1()
