from Equipments import *


class Inventory:
    def __init__(self):
        self.gold = 0
        self.equipement = Equipments()
        self.consumable = []

    def getGold(self):
        return self.gold