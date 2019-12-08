from Equipments import *
from Objects import *

#class that define the peace of equipemetns JEWEL
#A JEWEL has to attribute that improve HP and MP
class Jewel(Objects):
    def __init__(self):
        self.bonusHP = 0
        self.bonusMP = 0

    #Display information about the objects
    def show_stat_object(self):
        print("****************")
        print("  Object : Jewel")
        print("  HP : " + str(self.bonusHP))
        print("  MP : " + str(self.bonusMP))
        print("****************")

    #Generate a random JEWEL depending on the level in which you are
    def generate_random_jewel(self, level):
        jewel = Jewel()
        jewel.bonusHP = randint(int(level * 2), int(level * 5)) + 5
        jewel.bonusMP = randint(int(level * 2), int(level * 3)) + 10
        return jewel

    #Getters to acces to JEWEL stats
    def get_bonus_HP(self):
        return self.bonusHP

    def get_bonus_MP(self):
        return self.bonusMP
