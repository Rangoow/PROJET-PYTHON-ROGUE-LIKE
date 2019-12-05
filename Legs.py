from random import *
from Objects import *


class Legs(Objects):
    def __init__(self):
        self.bonusHP = 0
        self.bonusArmor = 0

    def show_stat_object(self):
        print("***************")
        print("  Object : Legs")
        print("  HP : " + str(self.bonusHP))
        print("  Armor : " + str(self.bonusArmor))
        print("***************")

    def generate_random_legs(self, level):
        legs = Legs()
        legs.bonusHP = randint(int(level * 3), int(level * 5))
        legs.bonusArmor = randint(int(level * 1), int(level * 2))
        return legs



    #Getters

    def get_bonus_HP(self):
        return self.bonusHP

    def get_bonus_armor(self):
        return self.bonusArmor