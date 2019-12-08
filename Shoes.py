from random import *
from Objects import *

#class that define the peace of equipemetns SHOES
#A SHOES has to attribute that improve HP and Armor
class Shoes(Objects):
    def __init__(self):
        self.bonusHP = 0
        self.bonusArmor = 0

    # Display information about the objects
    def show_stat_object(self):
        print("**************")
        print("  Object : Shoes")
        print("  HP : " + str(self.bonusHP))
        print("  Armor : " + str(self.bonusArmor))
        print("**************")

    # Generate a random SHOES depending on the level in which you are
    def generate_random_shoes(self, level):
        shoes = Shoes()
        shoes.bonusHP = randint(int(level * 2), int(level * 5)) + 10
        shoes.bonusArmor = randint(int(level * 2), int(level * 3))
        return shoes

    #Getters to acces to Shoes stats
    def get_bonus_HP(self):
        return self.bonusHP

    def get_bonus_armor(self):
        return self.bonusArmor