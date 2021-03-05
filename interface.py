from insert import add_dog

choice = input("Press 1 to add a dog.\n")

if choice == 1:
    name = raw_input("What is the name of the new dog?\n")
    add_dog(name)

