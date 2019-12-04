from Inventory import *
from abc import *


class Character(ABC):
    def __init__(self):
        self.HP = None
        self.maxHP = None
        self.MP = None
        self.minDamage = None
        self.maxDamage = None
        self.armor = None
        self.inventory = Inventory()

    def take_damage(self, damage):
        self.HP -= damage



