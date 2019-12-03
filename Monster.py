# coding=utf-8
from Character import *
from Equipments import *

class Monster(Character):
    def __init__(self):
        Character.__init__(self)
        self.inventory = None
        self.hp = 0
        self.max_hp = 0
        self.min_atk = 0
        self.max_atk = 0
        self.armor = 0

    #USED
    def generate_new_monster(self, level):
        self.lvl = level
        self.hp = randint(int(level * 2), int(level * 4))
        self.max_hp = self.hp
        self.min_atk = randint(int(level * 2), int(level * 4))
        self.max_atk = randint(int(level * 5), int(level * 7))
        self.armor = randint(int(level * 2), int(level * 4))

    #USED
    def generate_final_boss(self, level):
        self.lvl = level*5
        self.hp = 1000
        self.max_hp = self.max_hp
        self.min_atk = randint(int(level * 4), int(level * 6))
        self.max_atk = randint(int(level * 6), int(level * 8))
        self.armor = randint(int(level * 4), int(level * 6))

    def generate_loot(self, hero):
        min_xp = 1
        max_xp = 3
        random_stuff = randint(1, 6)
        if hero.requiredexp >10:
            min_xp = 2
            max_xp = 6
        elif hero.requiredexp > 40:
            min_xp = 4
            max_xp = 10
        hero.currentexp += randint(min_xp, max_xp)

        gold = randint(int(self.lvl * 3), int(self.lvl * 6))
        hero.inventory.gold += gold

        #1 chance on 3 to earn some new stuff
        tmp = randint(1,3)
        if tmp == 3:
            if random_stuff == 1:
                weapon = Weapon()
                weapon = Weapon.generate_random_weapon(self, hero.lvl + 1)
                print("Vous avez drop une weapon !")
                hero.inventory.equipement.loot.append(weapon)
            elif random_stuff == 2:
                jewel = Jewel()
                jewel = Jewel.generate_random_jewel(self, hero.lvl + 1)
                print("Vous avez droppé un nouveau jewel !")
                hero.inventory.equipement.loot.append(jewel)
            elif random_stuff == 3:
                head = Head()
                head = Head.generate_random_head(self, hero.lvl + 1)
                print("Vous avez droppé une head !")
                hero.inventory.equipement.loot.append(head)
            elif random_stuff == 4:
                chest = Chest()
                chest = Chest.generate_random_chest(self, hero.lvl + 1)
                print("Vous avez droppé un chest !")
                hero.inventory.equipement.loot.append(chest)
            elif random_stuff == 5:
                legs = Legs()
                legs = Legs.generate_random_legs(self, hero.lvl + 1)
                print("Vous avez droppé un legs !")
                hero.inventory.equipement.loot.append(legs)
            elif random_stuff == 6:
                shoes = Shoes()
                shoes = Shoes.generate_random_shoes(self, hero.lvl + 1)
                print("Vous avez droppé un shoes !")
                hero.inventory.equipement.loot.append(shoes)

    #USED
    def attack_monster(self, value):
        self.hp -= value
    #USED
    def reduce_atk_monster(self, value):
        print("Vous avez diminué l'attaque du monstre de ", value)
        self.min_atk -= 0.2 * self.min_atk
        self.max_atk -= 0.2 * self.max_atk

    #USED
    def attack_hero(self, hero):
        damage = randint(int(self.min_atk), int(self.max_atk))
        print("L'enemie vous a infligé ", damage, " dégats")
        hero.receive_damage(damage)
        print("Le hero possède maintenant ", hero.hp," points de vie")

    #USED
    def check_if_monster_is_dead(self):
        if self.hp > 0:
            print("Le monstre a", self.hp, "hp après votre attaque.")
            return False
        else:
            self.hp = 0
            print("Le monstre est mort après votre attaque.")
            return True