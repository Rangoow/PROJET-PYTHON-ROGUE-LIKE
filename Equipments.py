from Objects import *
from Weapon import *
from Jewel import *
from Head import *
from Chest import *
from Legs import *
from Shoes import *
from GameTestArchitecture import *
from Hero import *


class Equipments(Objects):
    def __init__(self):
        self.weapon = Weapon()
        self.jewel = Jewel()
        self.head = Head()
        self.chest = Chest()
        self.legs = Legs()
        self.shoes = Shoes()
        self.loot = []


    def generate_base_equipement(self, level):
        self.weapon = Weapon.generate_random_weapon(self, level)
        self.jewel = Jewel.generate_random_jewel(self, level)
        self.head = Head.generate_random_head(self, level)
        self.chest = Chest.generate_random_chest(self, level)
        self.legs = Legs.generate_random_legs(self, level)
        self.shoes = Shoes.generate_random_shoes(self, level)


    # To calculate a specific stat from all the stuff equiped
    def calculate_hp_from_stuff(self):
        return self.jewel.get_hp() + self.head.get_hp() + self.chest.get_hp() + self.legs.get_hp() + self.shoes.get_hp()

    def calculate_mp_from_stuff(self):
        return self.jewel.get_mp()

    def calculate_min_atk_from_stuff(self):
        return self.weapon.get_min_atk()

    def calculate_max_atk_from_stuff(self):
        return self.weapon.get_max_atk()

    def calculate_armor_from_stuff(self):
        return self.head.get_armor() + self.chest.get_armor() + self.legs.get_armor() + self.shoes.get_armor()






