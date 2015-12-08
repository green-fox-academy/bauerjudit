class Warrior:
    def __init__(self):
        self.companions = []

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.inflict_damage(10)

    def cursed(self, opponent):
        opponent.inflict_curse(10)

    def inflict_damage(self, damage):
        self.hp -= damage
        for companion in self.companions:
            companion.notify("damage", self)

    def inflict_curse(self, damage):
        self.hp -= damage
        for companion in self.companions:
            companion.notify("cursed", self)

    def heal(self, hp):
        self.hp += hp

    def remove_curse(self, hp):
        self.hp += hp


class Healer:
    def notify(self, type, warrior):
        if type == "damage":
            warrior.heal(10)

class RemoveCurse:
    def notify(self, type, warrior):
        if type == "cursed":
            warrior.heal(20)

rabbit = Warrior()
wolf = Warrior()
shaman = Healer()
rabbit.join(shaman)

witch = RemoveCurse()
rabbit.join(witch)




wolf.strike(rabbit)
print(rabbit.hp)
