class MenuItem():
    def __init__(self, num, name, action):
        self.num = num
        self.name = name
        self.action = action

    def __repr__(self):
       return '{} {}'.format(self.num, self.name)

class Menu():
    def __init__(self, items):
        self.items = items

    def choose (self, number):
        for item in self.items:
            if item.num == number:
                return item.action()

    def print_menu(self):
        for item in self.items:
            print(item)

    def user_input(self):
        try:
            user_input = int(input("Choose a number: "))
            if user_input == " " or user_input > len(self.items):
                raise ValueError
        except:
            print("Wrong input")
        return user_input

    def print_input_choose(self):
        self.print_menu()
        self.choose(self.user_input())

def add_character_name():
    name_input = input("Add character name: ")
    return name_input

def exit():
    pass

def print_status():
    print("dexterity:", "health:", "luck:")


def reroll_status_action():
    pass
    #refresh print_status

def begin_action():
    pass


def reselect_potion_action():
    reselect_potion_items = Menu([
        MenuItem(1, "Reselect Potion", potion_menu_action),
        MenuItem(2, "Continue", begin_action),
        MenuItem(3, "Quit", exit),
    ])
    #print potion status
    reselect_potion_items.print_input_choose()

def potion_menu_action():
    potion_menu_items = Menu([
        MenuItem(1, "Potion of Health", reselect_potion_action),
        MenuItem(2, "Potion of Dexterity", reselect_potion_action),
        MenuItem(3, "Potion of Luck", reselect_potion_action),
    ])
    potion_menu_items.print_input_choose()


def continue_action():
    continue_items = Menu([
        MenuItem(1, "Reroll status", reroll_status_action),
        MenuItem(2, "Continue", potion_menu_action),
        MenuItem(3, "Save", None),
        MenuItem(4, "Quit", exit)
    ])
    print_status()
    continue_items.print_input_choose()

def quit_action():
    quit_items = Menu([
        MenuItem(1, "Save and quit", None),
        MenuItem(2, "Quit and not save", exit),
        MenuItem(3, "Resume", None)
    ])
    quit_items.print_input_choose()


def new_game_action():
    new_game_items = Menu([
        MenuItem(1, "Reenter name", add_character_name),
        MenuItem(2, "Continue", continue_action),
        MenuItem(3, "Save", None),
        MenuItem(4, "Quit", quit_action),
        ])
    add_character_name()
    #new_game_items.print_menu()
    new_game_items.print_input_choose()

main_menu = Menu([
        MenuItem(1, "New Game", new_game_action),
        MenuItem(2, "Load Game", None),
        MenuItem(3, "Exit", exit),
    ])





#main_menu.print_menu()
#main_menu.choose(main_menu.user_input())
main_menu.print_input_choose()
