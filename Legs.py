from random import *
from Objects import *

#class that define the peace of equipemetns LEGS
#A LEGS has to attribute that improve HP and Armor
class Legs(Objects):
    def __init__(self):
        self.bonusHP = 0
        self.bonusArmor = 0

    # Display information about the objects
    def show_stat_object(self):
        print("***************")
        print("  Object : Legs")
        print("  HP : " + str(self.bonusHP))
        print("  Armor : " + str(self.bonusArmor))
        print("***************")

    # Generate a random LEGS depending on the level in which you are
    def generate_random_legs(self, level):
        legs = Legs()
        legs.bonusHP = randint(int(level * 2), int(level * 5)) + 15
        legs.bonusArmor = randint(int(level * 2), int(level * 3))
        return legs



    #Getters to acces to LEGS stats
    def get_bonus_HP(self):
        return self.bonusHP

    def get_bonus_armor(self):
        return self.bonusArmor