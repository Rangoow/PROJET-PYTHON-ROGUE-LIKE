from Equipments import *
from Objects import *


class Jewel(Objects):
    def __init__(self):
        self.bonusHP = 0
        self.bonusMP = 0

    def show_stat_object(self):
        print("****************")
        print("  Object : Jewel")
        print("  HP : " + str(self.bonusHP))
        print("  MP : " + str(self.bonusMP))
        print("****************")

    def generate_random_jewel(self, level):
        jewel = Jewel()
        jewel.bonusHP = randint(int(level * 4.3), int(level * 5.3))
        jewel.bonusMP = randint(int(level * 2), int(level * 3))
        return jewel

    # Getters

    def get_bonus_HP(self):
        return self.bonusHP

    def get_bonus_MP(self):
        return self.bonusMP
