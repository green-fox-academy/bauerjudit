class Game_Character:
    def __init__(self, name, health_points, demage):
        self.name = name
        self.health_points = health_points
        self.demage = demage

    def print_status(self):
        if self.health_points == 0:
            print(self.name)
            print("Dead")
        if self.health_points > 0:
            print(self.name)
            print(self.health_points)

    def drink_potion(self):
        self.health_points += 10


    def strike(self, other_character):
        other_character.health_points -= self.demage


class Cerlic(Game_Character):
    def heal(self, ally):
        ally.health_points += 10


Bence = Game_Character("Bence", 100, 60)
Gergo = Game_Character("Gergo", 150, 50)
Sebe = Cerlic("Sebe", 60, 60)

Bence.print_status()
Gergo.print_status()
for i in range(2):
    Bence.strike(Gergo)
Bence.print_status()
Gergo.print_status()
Sebe.heal(Gergo)
