from Objects import *
from Weapon import *
from Jewel import *
from Head import *
from Chest import *
from Legs import *
from Shoes import *

#Define all type of equipements available
#Based on minecrfat system head, chest, legs, shoes, weapon and we add jewel
class Equipments(Objects):
    def __init__(self):
        self.weapon = Weapon()
        self.jewel = Jewel()
        self.head = Head()
        self.chest = Chest()
        self.legs = Legs()
        self.shoes = Shoes()
        self.loot = []

    #generate the random first stuff when the player is created
    def first_stuff(self, level):
        self.weapon = Weapon.generate_random_weapon(self, level)
        self.jewel = Jewel.generate_random_jewel(self, level)
        self.head = Head.generate_random_head(self, level)
        self.chest = Chest.generate_random_chest(self, level)
        self.legs = Legs.generate_random_legs(self, level)
        self.shoes = Shoes.generate_random_shoes(self, level)


    #Calculate all the new stats based on the stuff equiped (HP / MP /DAMAGE / ARMOR)
    def stuff_HP(self):
        return self.jewel.get_bonus_HP() + self.head.get_bonus_HP() + self.chest.get_bonus_HP() + self.legs.get_bonus_HP() + self.shoes.get_bonus_HP()

    def stuff_MP(self):
        return self.jewel.get_bonus_MP()

    def stuff_min_damage(self):
        return self.weapon.get_min_damage()

    def stuff_max_damage(self):
        return self.weapon.get_max_damage()

    def stuff_armor(self):
        return self.head.get_bonus_armor() + self.chest.get_bonus_armor() + self.legs.get_bonus_armor() + self.shoes.get_bonus_armor()






