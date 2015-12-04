import commands
import sys


def menu():
        print("\033c")
        print('*************************************')
        print('* * *       1 List items        * * *')
        print('* *         2 Add new item        * *')
        print('*           3 Remove item           *')
        print('* *         4 Complete Item       * *')
        print('* * *       Q Exit Program      * * *')
        print('*************************************')


        choosen = input("Choose an option: ")
        if choosen == "1":
            print()
            print("\033c")
            commands.open_list()
            input("For menu hit enter ")
            menu()
        elif choosen == "2":
            commands.add_new_item()
            menu()
        elif choosen == "3":
            commands.remove()
            print()
            commands.open_list()
            menu()
        elif choosen == "4":
            menu()
        elif choosen == "Q":
            pass

menu()
