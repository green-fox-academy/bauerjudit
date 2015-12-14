menu_items = [{"name": "New Game"},
              {"name": "Load Game"},
              {"name": "Exit"}
]

new_game_items = [{"name": "Reenter name"},
                 {"name": "Continue"},
                 {"name": "Save"},
                 {"name": "Quit"}
]

class MyMenu():
    def __init__(self, menu_items):
        self.menu_items = menu_items

    def print_menu(self):
        for index, item in enumerate(self.menu_items):
            print(index + 1, item["name"])

    def exit(self):
        pass

    def menu_chooser(self):
        self.print_menu()
        try:
            chooser = int(input("Choose a number: "))
            #current = menu_items[chooser - 1]
            if chooser == "" or chooser > 3:
                raise ValueError
            elif chooser == 1:
                new_game_menu = NewGame(new_game_items)
                new_game_menu.new_game_menu_chooser()
            elif chooser == 3:
                self.exit()
        except:
            print("Wrong input")

    def exit(self):
        pass

main_menu = MyMenu(menu_items)
main_menu.menu_chooser()



class NewGame(MyMenu):
    def __init__(self, new_game_items):
        self.new_game_items = new_game_items

    def add_character_name(self):
        name_input = input("Choose a character name: ")
        print(name_input)

    def print_menu(self):
        for index, item in enumerate(self.new_game_items):
            print(index + 1, item["name"])

    def exit():
        pass

    def new_game_menu_chooser(self):
        self.add_character_name()
        self.print_menu()
        try:
            chooser = int(input("Choose a number: "))
            if chooser == "" or chooser > 4:
                raise ValueError
            elif chooser == 4:
                self.exit()
        except:
            print("Wrong number: ")
            self.print_menu
