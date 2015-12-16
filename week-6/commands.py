from random import randint
#from character import *

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

    def exit(self):
        pass


class Character():
    def __init__(self, name = None, dexterity= None, health = None, luck = None, potion = None):
        self.name = name
        self.dexterity = dexterity
        self.health = health
        self.luck = luck
        self.potion = potion

    def add_character_name(self):
        self.name = input("Add character name: ")
        return self.name

    def random_dexterity_health_luck(self):
        self.dexterity = randint(1, 6) + 6
        self.health = randint(2, 12) + 12
        self.luck = randint(1, 6) + 6
        return(print("dexterity:", self.dexterity, "health:", self.health, "luck:", self.luck))

    def choose_potion(self, potion):
        reselect_potion_action(potion)

    def inventory(self):
        return(print("Character name:", self.name, "Dexterity:", self.dexterity, "Health:", self.health, "Luck:", self.luck, "Potion:", self.potion))

class Enemy():
    def __init__(self, name = None, dexterity = None, health = None, luck = None):
        self.name = name
        self.dexterity = dexterity
        self.health = health
        self.luck = luck

    def enemy_inventory(self):
        return(print("dexterity:", self.dexterity, "health:", self.health, "luck:", self.luck))

class Strike():
    def __init__(self):

#def strike_method():


def strike_submenu_action():
    strike_submenu_items = Menu([
        MenuItem(1, "Continue", None),
        MenuItem(2, "Try your Luck", None),
        MenuItem(3, "Retreat", None),
        MenuItem(4, "Quit", exit)
    ])
    new_player.random_strike_dexterity()
    monster.random_strike_dexterity
    strike_submenu_items.print_input_choose()

def begin_action():
    begin_items = Menu([
        MenuItem(1, "Strike", None),
        MenuItem(2, "Retreat", None),
        MenuItem(3, "Quit", exit),
    ])
    new_player.inventory()
    begin_items.print_input_choose()


def reroll_status_action():
    new_player.random_dexterity_health_luck()
    continue_action()

def reselect_potion_action(potion):
    reselect_potion_items = Menu([
        MenuItem(1, "Reselect Potion", potion_menu_action),
        MenuItem(2, "Continue", begin_action),
        MenuItem(3, "Quit", exit),
    ])
    print(potion)
    reselect_potion_items.print_input_choose()

def potion_menu_action():
    potion_menu_items = Menu([
        MenuItem(1, "Potion of Health", lambda : new_player.choose_potion("Potion of Health")),
        MenuItem(2, "Potion of Dexterity", lambda : new_player.choose_potion("Potion of Dexterity")),
        MenuItem(3, "Potion of Luck", lambda: new_player.choose_potion("Potion of Luck")),
    ])
    potion_menu_items.print_input_choose()


def continue_action():
    continue_items = Menu([
        MenuItem(1, "Reroll status", reroll_status_action),
        MenuItem(2, "Continue", potion_menu_action),
        MenuItem(3, "Save", None),
        MenuItem(4, "Quit", exit)
    ])
    new_player.random_dexterity_health_luck()
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
        MenuItem(1, "Reenter name", new_game_action),
        MenuItem(2, "Continue", continue_action),
        MenuItem(3, "Save", None),
        MenuItem(4, "Quit", quit_action),
        ])
    new_player.add_character_name()
    new_game_items.print_input_choose()

main_menu = Menu([
        MenuItem(1, "New Game", new_game_action),
        MenuItem(2, "Load Game", None),
        MenuItem(3, "Exit", exit),
    ])


new_player = Character()
monster = Enemy()

main_menu.print_input_choose()
