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
        while True:
            try:
                user_input = int(input("Choose a number: "))
                if user_input == " " or user_input > len(self.items) or user_input < 0:
                    raise ValueError
                else:
                    return user_input
            except ValueError:
                print("Wrong input")
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
        action.reselect_potion_action(potion)

    def inventory(self):
        return(print("Character Name:", self.name, "Dexterity:", self.dexterity, "Health:", self.health, "Luck:", self.luck, "Potion:", self.potion))

class Enemy():
    def __init__(self, name = None, dexterity = None, health = None, luck = None):
        self.name = name
        self.dexterity = dexterity
        self.health = health
        self.luck = luck

    def random_dexterity_enemy(self):
        self.dexterity = randint(1, 6) + 6
        return self.dexterity

    def random_health_enemy(self):
        self.health = randint(2, 12) + 12
        return self.health

    def enemy_inventory(self):
        return(print("MONSTER Dexterity:", self.dexterity, "Health:", self.health, "Luck:", self.luck))

class Strike():
    def __init__(self, character_strike = None, enemy_strike = None):
        self.character_strike = character_strike
        self.enemy_strike = enemy_strike
    def strike_method(self):
        self.random_dexterity = randint(1, 6)
        self.random_dexterity = randint(1, 6)
        self.character_strike = self.random_dexterity + new_player.dexterity
        self.enemy_strike = self.random_dexterity + monster.dexterity
        if self.character_strike > self.enemy_strike:
            print("YOU HIT THE MONSTER")
        else:
            print("THE MONSTER HIT YOU")
    def after_strike_method(self):
        if self.character_strike > self.enemy_strike:
            monster.health -= 2
            print(monster.health)
        else:
            new_player.health -= 2
            print(new_player.health)
    def try_your_luck_method(self):
        self.random_luck = randint(2, 12)
        if self.random_luck > new_player.luck and self.character_strike < self.enemy_strike:
            new_player.health -= 3
            print("Health:", new_player.health)
        elif self.random_luck <= new_player.luck and self.character_strike < self.enemy_strike:
            new_player.health -= 1
            new_player.luck -= 1
            print("Health:", new_player.health, "Luck:", new_player.luck)
        elif self.random_luck <= new_player.luck and self.character_strike > self.enemy_strike:
            new_player.health -= 1
            print("Health:", new_player.health)
        else:
            new_player.health -= 4
            new_player.luck -= 1
            print("Health:", new_player.health, "Luck:", new_player.luck)

class Actions():
    def try_your_luck_action(self):
        fight.try_your_luck_method()
    def after_strike_action(self):
        begin_items = Menu([
            MenuItem(1, "Strike", action.strike_submenu_action),
            MenuItem(2, "Retreat", None),
            MenuItem(3, "Quit", exit),
        ])
        monster.random_health_enemy()
        fight.after_strike_method()
        begin_items.print_input_choose()
    def strike_submenu_action(self):
        strike_submenu_items = Menu([
            MenuItem(1, "Continue", action.after_strike_action),
            MenuItem(2, "Try your Luck", action.try_your_luck_action),
            MenuItem(3, "Retreat", None),
            MenuItem(4, "Quit", exit)
        ])
        fight.strike_method()
        strike_submenu_items.print_input_choose()
    def begin_action(self):
        begin_items = Menu([
            MenuItem(1, "Strike", action.strike_submenu_action),
            MenuItem(2, "Retreat", None),
            MenuItem(3, "Quit", exit),
        ])
        new_player.inventory()
        monster.random_dexterity_enemy()
        monster.random_health_enemy()
        monster.enemy_inventory()
        begin_items.print_input_choose()
    def reroll_status_action(self):
        new_player.random_dexterity_health_luck()
        action.continue_action()
    def reselect_potion_action(self, potion):
        reselect_potion_items = Menu([
            MenuItem(1, "Reselect Potion", action.potion_menu_action),
            MenuItem(2, "Continue", action.begin_action),
            MenuItem(3, "Quit", exit),
        ])
        print(potion)
        reselect_potion_items.print_input_choose()
    def potion_menu_action(self):
        potion_menu_items = Menu([
            MenuItem(1, "Potion of Health", lambda : new_player.choose_potion("Potion of Health")),
            MenuItem(2, "Potion of Dexterity", lambda : new_player.choose_potion("Potion of Dexterity")),
            MenuItem(3, "Potion of Luck", lambda: new_player.choose_potion("Potion of Luck")),
        ])
        potion_menu_items.print_input_choose()
    def continue_action(self):
        continue_items = Menu([
            MenuItem(1, "Reroll status", action.reroll_status_action),
            MenuItem(2, "Continue", action.potion_menu_action),
            MenuItem(3, "Save", None),
            MenuItem(4, "Quit", exit)
        ])
        new_player.random_dexterity_health_luck()
        continue_items.print_input_choose()
    def quit_action(self):
        quit_items = Menu([
            MenuItem(1, "Save and quit", None),
            MenuItem(2, "Quit and not save", exit),
            MenuItem(3, "Resume", None)
        ])
        quit_items.print_input_choose()
    def new_game_action(self):
        new_game_items = Menu([
            MenuItem(1, "Reenter name", action.new_game_action),
            MenuItem(2, "Continue", action.continue_action),
            MenuItem(3, "Save", None),
            MenuItem(4, "Quit", action.quit_action),
            ])
        new_player.add_character_name()
        new_game_items.print_input_choose()

action = Actions()

main_menu = Menu([
        MenuItem(1, "New Game", action.new_game_action),
        MenuItem(2, "Load Game", None),
        MenuItem(3, "Exit", exit),
    ])

new_player = Character()
monster = Enemy()
fight = Strike()

main_menu.print_input_choose()
