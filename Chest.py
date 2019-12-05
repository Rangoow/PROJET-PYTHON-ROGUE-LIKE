from random import *
from Objects import *


class Chest(Objects):
    def __init__(self):
        self.bonusHP = 0
        self.bonusArmor = 0

    def show_stat_object(self):
        print("****************")
        print("  Object : Chest")
        print("  HP : " + str(self.bonusHP))
        print("  Armor : " + str(self.bonusArmor))
        print("****************")

    def generate_random_chest(self, level):
        chest = Chest()
        chest.bonusHP = randint(int(level * 3), int(level * 5))
        chest.bonusArmor = randint(int(level * 1), int(level * 2))
        return chest

    # Getters

    def get_bonus_HP(self):
        return self.bonusHP

    def get_bonus_armor(self):
        return self.bonusArmor
