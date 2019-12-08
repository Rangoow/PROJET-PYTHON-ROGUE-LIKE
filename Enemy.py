# coding=utf-8
from Character import *
from Equipments import *

class Enemy(Character):
    def __init__(self):
        Character.__init__(self)
        self.HP = 0
        self.maxHP = 0
        self.minDamage = 0
        self.maxDamage = 0
        self.armor = 0

    #generate an enemy with random stats based on the level
    def generate_enemy(self, level):
        self.lvl = level
        self.HP = randint(int(level * 4), int(level * 6)) + 20
        self.maxHP = self.HP
        self.minDamage = randint(int(level * 2), int(level * 3))
        self.maxDamage = randint(int(level * 3), int(level * 5))
        self.armor = randint(int(level), int(level * 4))

    #generate the final boss with some random stats depending on the level which is always the last one
    def generate_final_boss(self, level):
        self.lvl = level*5
        self.HP = 1000
        self.maxHP = self.maxHP
        self.minDamage = randint(int(level * 4), int(level * 6))
        self.maxDamage = randint(int(level * 6), int(level * 8))
        self.armor = randint(int(level * 4), int(level * 6))

    #generate randomly gold, XP and loot after an enemy death
    def generate_loot(self, hero):
        minXP = 1
        maxXP = 3
        random_stuff = randint(1, 6)
        if hero.nextLevelXP >10:
            minXP = 2
            maxXP = 6
        elif hero.nextLevelXP > 40:
            minXP = 4
            maxXP = 10
        hero.XP += randint(minXP, maxXP)

        gold = randint(int(self.lvl * 3), int(self.lvl * 6))
        hero.inventory.gold += gold

        #1 chance on 3 to earn some new stuff
        tmp = randint(1,3)
        if tmp == 3:
            if random_stuff == 1:
                weapon = Weapon.generate_random_weapon(self, hero.heroLevel + 1)
                print("You've droped a weapon !")
                hero.inventory.equipement.loot.append(weapon)
            elif random_stuff == 2:
                jewel = Jewel.generate_random_jewel(self, hero.heroLevel + 1)
                print("You've droped a jewel !")
                hero.inventory.equipement.loot.append(jewel)
            elif random_stuff == 3:
                head = Head.generate_random_head(self, hero.heroLevel + 1)
                print("You've droped an head !")
                hero.inventory.equipement.loot.append(head)
            elif random_stuff == 4:
                chest = Chest.generate_random_chest(self, hero.heroLevel + 1)
                print("You've droped a chest !")
                hero.inventory.equipement.loot.append(chest)
            elif random_stuff == 5:
                legs = Legs.generate_random_legs(self, hero.heroLevel + 1)
                print("You've droped legs !")
                hero.inventory.equipement.loot.append(legs)
            elif random_stuff == 6:
                shoes = Shoes.generate_random_shoes(self, hero.heroLevel + 1)
                print("You've droped shoes !")
                hero.inventory.equipement.loot.append(shoes)

    #permit the hero to attack the enemy and reduce his health
    def attack_enemy(self, value):
        self.HP -= value

    #permit the player to reduce the enemy attack from 25%
    def reduce_enemy_attack(self, value):
        self.minDamage -= 0.25 * self.minDamage
        self.maxDamage -= 0.25 * self.maxDamage
        print("You reduce the enemy attack to : " + str(value))

    #Permit the enemy to attack the hero and reduce his health
    def attack_hero(self, hero):
        damage = randint(int(self.minDamage), int(self.maxDamage))
        hero.receive_damage(damage)
        print("The enemy deals you : " + str(damage) + " damages")
        print("You have : " + str(hero.HP) + " HP")

    #Check if the enmy is still alive or not and return a boolean (True = dead / False = alive)
    def check_enemy_state(self):
        if self.HP > 0:
            print("The enemy has : " + str(self.HP) + "HP after your attack")
            return False
        else:
            self.HP = 0
            print("The enemy is dead after your attack !")
            return True