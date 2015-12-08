from character import Character

class Cerlic(Character):
    def heal(self, other):
        other.hp += 10
