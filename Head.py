from random import *
from Objects import *


class Head(Objects):
    def __init__(self):
        self.bonusHP = 0
        self.bonusArmor = 0

    def show_stat_object(self):
        print("***************")
        print("  Object : Head")
        print("  HP : " + str(self.bonusHP))
        print("  Armor : " + str(self.bonusArmor))
        print("***************")

    def generate_random_head(selfself, level):
        head = Head()
        head.bonusHP = randint(int(level * 3), int(level * 5))
        head.bonusArmor = randint(int(level * 1), int(level * 2))
        return head

    #Getters
    def get_bonus_HP(self):
        return self.bonusHP

    def get_bonus_armor(self):
        return self.bonusArmor


