from random import *
from Objects import *


class Legs(Objects):
    def __init__(self):
        self.object = "legs"
        self.hp = 0
        self.armor = 0
        #self.gold_value = 5

    def show_stat_object(self):
        print("Object : \t Legs")
        print("HP : " + str(self.hp))
        print("Armor : " + str(self.armor))
        print("")

    def generate_random_legs(selfself, level):
        legs = Legs()
        legs.hp = randint(int(level * 3), int(level * 5))
        legs.armor = randint(int(level * 1), int(level * 2))
        return legs



    #Getters

    def get_hp(self):
        return self.hp

    def get_armor(self):
        return self.armor