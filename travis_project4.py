#create known users

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

print(len(known_users))

#using while true and if to remove names in a list and then confirming it
# to cancel a loop, hold ctrl + c
while True:
    print("Hello! My name is travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (Y/N)?: ").lower()
        
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
                print("No problem, I did not want you to leave anyways!")
            
            
    else:
        print("Hmmm I do not think I have met you yet {}".format(name))
        add = input("Would you like to be added to the system (Y/N)?: ").lower()
        if add == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif add == "n":
                print("No worries, see you around!")
                
#when the arrangement of elements is not known, using deleting of index is done
L = [1, 2, 3, 4, 5]
del L[0]
print(L)
L.remove(1)
print(L)
