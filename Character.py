from Inventory import *

#Mother class that define all properties that will have our hero and the enemies
class Character:
    def __init__(self):
        self.HP = None
        self.maxHP = None
        self.minDamage = None
        self.maxDamage = None
        self.MP = None
        self.armor = None
        self.inventory = Inventory()

    def take_damage(self, damage):
        self.HP -= damage



