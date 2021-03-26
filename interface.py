from insert import add_dog, add_food


run_program = 1

while run_program != 0:
    print "Press 1 to add a dog.\nPress 2 to add a food.\nPress 0 to quit."
    choice = input()
    
    if choice == 1:
        name = raw_input("What is the name of the new dog?\n")
        add_dog(name)

    elif choice ==2:
        name = raw_input("What is the name of the food?\n")
        wet = raw_input("Press 1 if the food is dry or 2 if the food is wet.\n")
        add_food(name, wet)

    elif choice == 0:
        run_program = 0

