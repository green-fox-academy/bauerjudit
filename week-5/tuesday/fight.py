class Weapon:

    def strike(self, warrior, opponent):
        warriro.hp -= self.damage()
        opponent.hp -= self.self_damage()

    def damage(self):
        raise "Not implemented"

    def self_damage(self):
        raise "Not implemented"

class Sword:
    def damage(self):
        return 10
    def self_damage(self):
        return 0

class FlameThrow:
    def damage(self):
        return 50
    def self_damage(self):
        return 20

class Enchanted(Weapon):
    def __init__(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() + 2

    def self_damage(self):
        return self.weapon.damage() + 2


class Warrior:
    def __init__(self, weapon):
        self.weapon = weapon
        self.hp = 100

    def strike(self, opponent):
        self.weapon.strike(self, opponent)

    def __repr__(self):
        return("Warrior hp={}".format(self.hp))


warrior = Warrior (Sword())
monster = Warrior(FlameThrow())


warrior.strike(monster)
print(warrior)
print(monster)

monster.strike(warriro)
print(warrior)
print(monster)
