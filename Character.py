from Inventory import *
from abc import *


class Character(ABC):
    def __init__(self):
        self.hp = None
        self.max_hp = None
        self.mp = None
        self.min_atk = None
        self.max_atk = None
        self.armor = None
        self.inventory = Inventory()

    def take_damage(self, damage):
        self.hp -= damage



