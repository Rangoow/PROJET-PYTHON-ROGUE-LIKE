from random import *
from Objects import *


class Head(Objects):
    def __init__(self):
        self.object = "head"
        self.hp = 0
        self.armor = 0
       #self.gold_value = 5

    def show_stat_object(self):
        print("Object : \t Head")
        print("HP : "+ str(self.hp))
        print("Armor : " + str(self.armor))
        print("")

    def generate_random_head(selfself, level):
        head = Head()
        head.hp = randint(int(level*3), int(level *5))
        head.armor = randint(int(level*1), int(level *2))
        return head




    #Getters

    def get_hp(self):
        return self.hp

    def get_armor(self):
        return self.armor


