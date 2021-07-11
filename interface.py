from insert import add_dog, add_food, add_adopter, add_adoption, query_adopter
from insert import query_dog

run_program = 1

while run_program != 0:
    print "Press 1 to add a dog.\nPress 2 to add a food."
    print "Press 3 to add a new adopter.\nPress 0 to quit."
    print "Press 4 to add a new adoption record."
    choice = input()
    
    if choice == 1:
        name = raw_input("What is the name of the new dog?\n")
        add_dog(name)

    elif choice == 2:
        name = raw_input("What is the name of the food?\n")
        wet = raw_input("Press 1 if the food is dry or 2 if the food is wet.\n")
        add_food(name, wet)

    elif choice == 3:
        first_name = raw_input("What is the first name of the new adopter?\n")
        last_name = raw_input("What is the last name of the new adopter?\n")
        email = raw_input("What is the adopter's email?\n")
        add_adopter(first_name, last_name, email)

    elif choice == 4:
        email = raw_input("What is the adopter's email?\n")
        name = raw_input("What is the name of the dog?\n")
        adopter_id = query_adopter(email)
        dog_id = query_dog(name)
        if adopter_id == None or dog_id == None:
            print "User/dog does not exist."
        else:
            add_adoption(adopter_id,dog_id)


    elif choice == 0:
        run_program = 0

