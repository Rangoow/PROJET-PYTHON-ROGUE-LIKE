from random import *
from Objects import *


class Shoes(Objects):
    def __init__(self):
        self.bonusHP = 0
        self.bonusArmor = 0


    def show_stat_object(self):
        print("**************")
        print("  Object : Shoes")
        print("  HP : " + str(self.bonusHP))
        print("  Armor : " + str(self.bonusArmor))
        print("**************")

    def generate_random_shoes(self, level):
        shoes = Shoes()
        shoes.bonusHP = randint(int(level * 3), int(level * 5))
        shoes.bonusArmor = randint(int(level * 1), int(level * 2))
        return shoes


    #Getters

    def get_bonus_HP(self):
        return self.bonusHP

    def get_bonus_armor(self):
        return self.bonusArmor