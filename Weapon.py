from Equipments import *
from random import *
from Objects import *


class Weapon(Objects):
    def __init__(self):
        self.minDamage = 0
        self.maxDamage = 0


    def show_stat_object(self):
        print("*****************")
        print("  Object : Weapon")
        print("  Attack range : " + str(self.minDamage) + " - " + str(self.maxDamage))
        print("*****************")

    def generate_random_weapon(self, level):
        weapon = Weapon()
        weapon.minDamage = randint(int(level * 2.3), int(level * 2.7))
        weapon.maxDamage = randint(int(level * 3.3), int(level * 3.7))
        return weapon

    # Getters

    def get_min_damage(self):
        return self.minDamage

    def get_max_damage(self):
        return self.maxDamage
