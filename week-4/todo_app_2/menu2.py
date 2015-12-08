from commands2 import *

def menu():
    print("***************************************")
    print("        1 List items                   ")
    print("        2 Add new item                 ")
    print("        3 Remove item                  ")
    print("***************************************")


    navigate = input("Choose a number: ")

    if navigate == "1":
        list_items()
    elif navigate == "2":
        add_item()
    else:
        navigate == "3"
        remove_item()

menu()
