from Equipments import *

#Inventory is composed of peace of equipements and gold
class Inventory:
    def __init__(self):
        self.gold = 0
        self.equipement = Equipments()

    #get the amount of gold you have
    def getGold(self):
        return self.gold