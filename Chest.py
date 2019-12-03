from random import *
from Objects import *


class Chest(Objects):
    def __init__(self):
        self.object = "chest"
        self.hp = 0
        self.armor = 0
        #self.gold_value = 5

    def show_stat_object(self):
        print("Object : \t Chest")
        print("hp : ", self.hp)
        print("armor : ", self.armor)
        print("")

    def generate_random_chest(selfself, level):
        chest = Chest()
        chest.hp = randint(int(level * 3), int(level * 5))
        chest.armor = randint(int(level * 1), int(level * 2))
        return chest

    # Getters

    def get_hp(self):
        return self.hp

    def get_armor(self):
        return self.armor
