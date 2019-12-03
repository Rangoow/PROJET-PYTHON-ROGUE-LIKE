from Equipments import *
from random import *
from Objects import *


class Weapon(Objects):
    def __init__(self):
        self.object = "weapon"
        self.min_atk = 0
        self.max_atk = 0
        #self.gold_value = 5


    def show_stat_object(self):
        print("Object : \t Weapon")
        print("Attack range : " + str(self.min_atk) + " - " + str(self.max_atk))
        print("")

    def generate_random_weapon(self, level):
        weapon = Weapon()
        weapon.min_atk = randint(int(level * 2.3), int(level * 2.7))
        weapon.max_atk = randint(int(level * 3.3), int(level * 3.7))
        return weapon

    # Getters

    def get_min_atk(self):
        return self.min_atk

    def get_max_atk(self):
        return self.max_atk
