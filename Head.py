from random import *
from Objects import *

#class that define the peace of equipemetns HEAD
#A HEAD has to attribute that improve HP and Armor
class Head(Objects):
    def __init__(self):
        self.bonusHP = 0
        self.bonusArmor = 0

    # Display information about the objects
    def show_stat_object(self):
        print("***************")
        print("  Object : Head")
        print("  HP : " + str(self.bonusHP))
        print("  Armor : " + str(self.bonusArmor))
        print("***************")

    # Generate a random HEAD depending on the level in which you are
    def generate_random_head(selfself, level):
        head = Head()
        head.bonusHP = randint(int(level * 2), int(level * 5)) + 15
        head.bonusArmor = randint(int(level * 2), int(level * 3)) + 5
        return head

    #Getters to acces to HEAD stats
    def get_bonus_HP(self):
        return self.bonusHP

    def get_bonus_armor(self):
        return self.bonusArmor


