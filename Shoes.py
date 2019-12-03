from random import *
from Objects import *


class Shoes(Objects):
    def __init__(self):
        self.object = "shoes"
        self.hp = 0
        self.armor = 0
        #self.gold_value = 5


    def show_stat_object(self):
        print("Object : \t Shoes")
        print("HP : " + str(self.hp))
        print("Armor : "+ str(self.armor))
        print("")

    def generate_random_shoes(selfself, level):
        shoes = Shoes()
        shoes.hp = randint(int(level * 3), int(level * 5))
        shoes.armor = randint(int(level * 1), int(level * 2))
        return shoes


    #Getters

    def get_hp(self):
        return self.hp

    def get_armor(self):
        return self.armor