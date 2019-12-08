from Equipments import *
from random import *
from Objects import *

#class that define the peace of equipemetns WEAPON
#A WEAPON has to attribute that improve attack
class Weapon(Objects):
    def __init__(self):
        self.minDamage = 0
        self.maxDamage = 0

    # Display information about the objects
    def show_stat_object(self):
        print("*****************")
        print("  Object : Weapon")
        print("  Attack range : " + str(self.minDamage) + " - " + str(self.maxDamage))
        print("*****************")

    # Generate a random WEAPON depending on the level in which you are
    def generate_random_weapon(self, level):
        weapon = Weapon()
        weapon.minDamage = randint(int(level * 2), int(level * 3))
        weapon.maxDamage = randint(int(level * 3), int(level * 4))
        return weapon

    #Getters to acces to WEAPON stats
    def get_min_damage(self):
        return self.minDamage

    def get_max_damage(self):
        return self.maxDamage
