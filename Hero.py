# coding=utf-8
from Character import *



class Hero(Character):

    def __init__(self):
        Character.__init__(self)
        self.name = ""
        self.classe = ""
        self.lvl = 1
        self.next_level_xp = 1
        self.xp = 0
        ###Base attribute
        self.hp = 50
        self.max_hp = 50
        self.mp = 100
        self.min_atk = 5
        self.max_atk = 10
        self.armor = 5
        self.number_of_hp_pots = 1
        self.number_of_mp_pots = 1
        self.restLeft = 1
        self.inventory.equipement.generate_base_equipement(self.lvl) ## Pour donner des armes des base
        self.stats_improve_from_stuff()

    def setHp(self):
        self.hp = self.max_hp

    def setName(self, name):
        self.name = name

    def setClass(self, classe):
        if classe == 1:
            self.classe = "Naruto Runner"
        elif classe == 2:
            self.classe = "Berzerk"
        elif classe == 3:
            self.classe = "Stone Thrower"
        else:
            self.classe = "noob"

    #modify the display add style
    def printIdentity(self):
        print("Mon nom d'aventurier est " + self.name + ", je suis un " + self.classe)

    #modify the display add style
    def displayStat(self):
        print("Je suis un " + self.classe + " de niveau " + str(self.lvl) + ", je possède " +str(self.hp)+ "/" + str(self.max_hp) + " points de vies. J'ai également " + str(self.min_atk) + " points d'attaques, " + str(self.armor) + " points de defence.")
        print("requiredxp : " + str(self.next_level_xp) + "  currentxp : " + str(self.xp) + "  max atk : " + str(self.max_atk))
        print("mp : " + str(self.mp))
        print("Gold : " + str(self.inventory.getGold()))


    #Getters & Setters

    def get_hp(self):
        return self.hp

    def get_lvl(self):
        return self.lvl

    # USED
    def show_skill_in_book(self):
        print("You have 3 different skill :  ")
        print(" (1) skill 1 : Deal hight damage to a monster : cost 20 mp")
        print(" (2) skill 2 : Give back 20% of hero's life : cost 30 mp")
        print(" (3) skill 3 : Reduce enemy's attack by 25% : cost 20 mp")

    # USED
    def mana_available_check(self, spell):  #We check if we can cast the spell  #20 30 15 30 20
        if spell == 1:
            return True if self.mp >= 20 else False
        elif spell == 2:
            return True if self.mp >= 30 else False
        elif spell == 3:
            return True if self.mp >= 15 else False

    #USED
    def stats_improve_from_stuff(self): #To calculate the stat after the aquisition of a new equipement
        ###Base attributs + Equipments Attributs
        if self.hp == 50:
            self.hp = self.max_hp
        self.max_hp += self.inventory.equipement.calculate_hp_from_stuff()
        self.hp += self.inventory.equipement.calculate_hp_from_stuff()
        self.mp += self.inventory.equipement.calculate_mp_from_stuff()
        self.min_atk += self.inventory.equipement.calculate_min_atk_from_stuff()
        self.max_atk += self.inventory.equipement.calculate_max_atk_from_stuff()
        self.armor += self.inventory.equipement.calculate_armor_from_stuff()

    # USED
    def stats_improve_from_level_up(self):
        self.max_hp += 2*self.lvl
        self.hp = self.max_hp # We give the life back of the hero
        self.mp += 2*self.lvl
        self.min_atk += 2*self.lvl
        self.max_atk += 2*self.lvl
        self.armor += 2*self.lvl

    # USED
    def check_for_level_up(self):
        while self.xp >= self.next_level_xp:
            self.lvl += 1
            self.mp += 10
            self.xp -= self.next_level_xp
            self.next_level_xp += 2
            self.stats_improve_from_level_up()
            print("################")
            print("YOU LEVEL UP !!!")
            print("################")

    # USED
    def basic_attack(self, enemy):
        damage = randint(self.min_atk, self.max_atk)
        print("You hit the enemy and deal : "+ str(damage) + " damages.")
        enemy.attack_enemy(damage)

    # USED
    def receive_damage(self, value):
        self.hp -= value

    # USED
    def magic_skill_1(self, enemy): #Like the basic attack, but strongest
        damage = 2 * (randint(self.min_atk, self.max_atk))
        print("You strongly hit the enemy and deal :" + str(damage) + " damages.")
        enemy.attack_enemy(damage)
        self.mp -= 20

    # USED
    def magic_skill_2(self): #Give back 15% of the hero max hp
        heal = self.max_hp * 0.20
        if self.hp + heal >= self.max_hp:
            print("You ")
            self.hp = self.max_hp
        else:
            print("After your healing incantation ou have now : " + str(self.hp) + " HP")
            self.hp += heal
        self.mp -= 30

    # USED
    def magic_skill_3(self, enemy):  #Reduce the monster attack by 20%
        value = 2 * self.lvl
        enemy.reduce_enemy_attack(value)
        self.mp -= 20

    # USED but to modify
    def change_equipement(self):
        loot = self.inventory.equipement.loot
        weapon = self.inventory.equipement.weapon
        jewel = self.inventory.equipement.jewel
        head = self.inventory.equipement.head
        chest = self.inventory.equipement.chest
        legs = self.inventory.equipement.legs
        shoes = self.inventory.equipement.shoes
        print("There are", len(loot), "peace of equipment in your inventory, let's take a look at it :")
        for i in range(len(loot)):
            item = loot[i]
            if isinstance(loot[i], Weapon):
                print("Object " + str(i + 1) + " : Weapon ")
                print("Weapon equiped : ")
                weapon.show_stat_object()
                print("Weapon from the inventory : ")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(weapon, item)
                else:
                    print("Don't change the weapon !")

            elif isinstance(loot[i], Jewel):
                print("Object " + str(i + 1) + " : Jewel ")
                print("Jewel equiped : ")
                jewel.show_stat_object()
                print("Jewel from the inventory : ")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(jewel, item)
                else:
                    print("Don't change the jewel !")

            elif isinstance(loot[i], Head):
                print("Object " + str(i + 1) + " : Head ")
                print("Head equiped : ")
                head.show_stat_object()
                print("Head from the inventory : ")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(head, item)
                else:
                    print("Don't change the head !")

            elif isinstance(loot[i], Chest):
                print("Object " + str(i + 1) + " : Chest ")
                print("Chest equiped : ")
                chest.show_stat_object()
                print("Chest from the inventory: ")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(chest, item)
                else:
                    print("Don't change the chest !")

            elif isinstance(loot[i], Legs):
                print("Object " + str(i + 1) + " : Legs ")
                print("Legs equiped : ")
                legs.show_stat_object()
                print("Legs from the inventory")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(legs, item)
                else:
                    print("Don't change the legs !")

            elif isinstance(loot[i], Shoes):
                print("Object " + str(i + 1) + " : SHoes ")
                print("Shoes equiped : ")
                shoes.show_stat_object()
                print("shoes from the inventory : ")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(shoes, item)
                    tmp = shoes
                    shoes = item
                    item = tmp
                else:
                    print("Don't change the shoes !")
            print("#####################")
            input("     Press enter     ")
            print("#####################")

    # USED but to modify
    def want_to_change_armor(self):
        print("Do you want to trade equipment 1 for equipement 2 ? ")
        print(" (1) Yes")
        print(" (2) No ")
        print("-------------------------------------------------------------------------")
        while True:
            choice = input("")
            try:
                if int(choice) == 1:
                    return 1
                elif int(choice) == 2:
                    return 2

                else:
                    print("Please enter a correct value !")

            except ValueError:
                print("Please enter a correct value !")

    # USED but to modify
    def swap_stuff(self, stuff_equiped, stuuf_from_inventory):
        print("You succesfully change your're stuff")
        tempo = stuff_equiped
        stuff_equiped = stuuf_from_inventory
        stuuf_from_inventory = tempo
        #if isinstance(stuff_equiped, Weapon):
        new_min_attack = stuff_equiped.min_atk - stuuf_from_inventory.min_atk
        new_max_attack = stuff_equiped.max_atk - stuuf_from_inventory.max_atk
        self.min_atk += new_min_attack
        self.max_atk += new_max_attack
        #elif isinstance(stuff_equiped, Jewel):
        new_hp = stuff_equiped.hp - stuuf_from_inventory.hp
        new_mp = stuff_equiped.mp - stuuf_from_inventory.mp
        self.max_hp += new_hp
        self.mp += new_mp
        #else:
        new_hp = stuff_equiped.hp - stuuf_from_inventory.hp
        new_armor = stuff_equiped.armor - stuuf_from_inventory.armor
        self.max_hp += new_hp
        self.armor += new_armor

