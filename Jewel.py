from Equipments import *
from Objects import *


class Jewel(Objects):
    def __init__(self):
        self.object = "jewel"
        self.hp = 0
        self.mp = 0
        self.gold_value = 5

    def __str__(self):
        return "Jewel"

    def show_stat_object(self):
        print("Object : \t Jewel")
        print("HP : " + str(self.hp))
        print("MP : " + str(self.mp))
        print("")

    def generate_random_jewel(self, level):
        jewel = Jewel()
        jewel.hp = randint(int(level * 4.3), int(level * 5.3))
        jewel.mp = randint(int(level * 2), int(level * 3))
        return jewel

    # Getters

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp
