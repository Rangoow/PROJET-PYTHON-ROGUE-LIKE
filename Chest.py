from random import *
from Objects import *

#class that define the peace of equipemetns CHEST
#A CHEST has to attribute that improve HP and Armor
class Chest(Objects):
    def __init__(self):
        self.bonusHP = 0
        self.bonusArmor = 0

    #Display information about the objects
    def show_stat_object(self):
        print("****************")
        print("  Object : Chest")
        print("  HP : " + str(self.bonusHP))
        print("  Armor : " + str(self.bonusArmor))
        print("****************")

    #Generate a random CHEST depending on the level in which you are
    def generate_random_chest(self, level):
        chest = Chest()
        chest.bonusHP = randint(int(level * 2), int(level * 5)) + 20
        chest.bonusArmor = randint(int(level * 2), int(level * 3)) + 5
        return chest

    #Getters to acces to CHEST stats
    def get_bonus_HP(self):
        return self.bonusHP

    def get_bonus_armor(self):
        return self.bonusArmor
