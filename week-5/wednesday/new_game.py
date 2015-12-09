class Character():
    def __init__(self, health = 20, armor = 10):
        self._health = health
        self._armor = armor
        self._isAlive = True

    def sufferDamage(self, damage):
        sufferDamage = self._health + self._armor - damage

        if sufferDamage < 1:
            self._isAlive = False

    def heal(self, heal):
        self._health += heal

    def isAlive(self):
        return self._isAlive

    def getHealth(self):
        return self._health

def handleEvents(events):
    eventHandlers = (
        "damage": applyDamage,
        "heal": applyHeal
    )

    



def handleEvents(eventList):
    filter_damage = list(filter(lambda x: x["type"] == "damage", eventList))
    list(map(lambda x : x["character"].sufferDamage(x["size"]), filter_damage))

def handleHealEvents(eventList):
    filter_heal = list(filter(lambda x: x["type"] == "heal", eventList))
    list(map(lambda x : x["character"].heal(x["size"]), filter_heal))
