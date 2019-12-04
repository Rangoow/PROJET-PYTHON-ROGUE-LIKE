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

    #USED
    def description_skill1_display(self):
        print("Sort 1 : Sort qui inflige de gros dégats sur un monstre : coûte 20 mp")

    # USED
    def description_skill2_display(self):
        print("Sort 2 : Redonne 15% de sa vie au héros : coûte 30 mp")

    # USED
    def description_skill3_display(self):
        print("Sort 3 : Reduit l'attaque d'un monstre de 20% : coûte 20 mp")

    # USED
    def show_skill_in_book(self):
        print("Vous avez 3 sorts a disposition : ")
        self.description_skill1_display()
        self.description_skill2_display()
        self.description_skill3_display()

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
            print("Vous avez gagné un niveau")

    # USED
    def basic_attack(self, monster):
        damage = randint(self.min_atk, self.max_atk)
        print("Vous attaquez le monstre et fait ", damage, "dégats.")
        monster.attack_monster(damage)

    # USED
    def receive_damage(self, value):
        self.hp -= value

    #CHANGE SPELL DEPENDING ON THE HERO'S CLASS (WITH IF self.class == ...)
    # USED
    def magic_skill_1(self, monster): #Like the basic attack, but strongest
        damage = 2 * (randint(self.min_atk, self.max_atk))
        print("Vous attaquez le monstre en faisait", damage, "dégats.")
        monster.attack_monster(damage)
        self.mp -= 20

    # USED
    def magic_skill_2(self): #Give back 15% of the hero max hp
        heal = self.max_hp * 0.15
        if self.hp + heal >= self.max_hp:
            print("Vous avez recuperer toutes votre vie")
            self.hp = self.max_hp
        else:
            print("Après le soin, vous avez", self.hp," points de vies")
            self.hp += heal
        self.mp -= 30

    # USED
    def magic_skill_3(self, monster):  #Reduce the monster attack by 20%
        value = 2 * self.lvl
        monster.reduce_enemy_attack(value)
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
        print("Il y a", len(loot), "objets dans votre inventaire, nous allons regarder si ces derniers vous interessent : ")
        for i in range(len(loot)):
            item = loot[i]
            if isinstance(loot[i], Weapon):
                print("L'item ", i + 1, "de l'inventaire est un weapon")
                print("Arme équipée : ")
                weapon.show_stat_object()
                print("Arme de l'inventaire : ")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(weapon, item)
                else:
                    print("On ne change pas d'arme")

            elif isinstance(loot[i], Jewel):
                print("L'item ", i + 1, "de l'inventaire est un jewel")
                print("Jewel équipé : ")
                jewel.show_stat_object()
                print("Jewel de l'inventaire : ")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(jewel, item)
                else:
                    print("On ne change pas de jewel")

            elif isinstance(loot[i], Head):
                print("L'item ", i + 1, "de l'inventaire est une head")
                print("Head équipé : ")
                head.show_stat_object()
                print("Head de l'inventaire : ")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(head, item)
                else:
                    print("On ne change pas d'head")

            elif isinstance(loot[i], Chest):
                print("L'item ", i + 1, "de l'inventaire est un chest")
                print("Chest équipé : ")
                chest.show_stat_object()
                print("Chest de l'inventaire : ")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(chest, item)
                else:
                    print("On ne change pas de chest")

            elif isinstance(loot[i], Legs):
                print("L'item ", i + 1, "de l'inventaire est un leg")
                print("Legs équipé : ")
                legs.show_stat_object()
                print("Legs de l'inventaire : ")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(legs, item)
                else:
                    print("On ne change pas de legs")

            elif isinstance(loot[i], Shoes):
                print("L'item ", i + 1, "de l'inventaire est des shoes")
                print("shoes équipé : ")
                shoes.show_stat_object()
                print("shoes de l'inventaire : ")
                item.show_stat_object()
                choice = self.want_to_change_armor()
                if int(choice) == 1:
                    self.swap_stuff(shoes, item)
                    tmp = shoes
                    shoes = item
                    item = tmp
                else:
                    print("On ne change pas de shoes")

            input("Presse enter")

    # USED but to modify
    def want_to_change_armor(self):
        print("Voulez vous changer l'équipement : 1 Pour changer ,0 pour ne rien changer")
        print("-------------------------------------------------------------------------")
        while True:
            choice = input("")
            try:
                if int(choice) == 1:
                    return 1
                elif int(choice) == 0:
                    return 0

                else:
                    print("Valeur invalide, essayer encore")

            except ValueError:
                print("Valeur invalide, essayer encore")

    # USED but to modify
    def swap_stuff(self, weapon_equiped, new_weapon):
        print("You succesfully change your're stuff")
        tempo = weapon_equiped
        weapon_equiped = new_weapon
        new_weapon = tempo
        if isinstance(weapon_equiped, Weapon):
            new_min_attack = weapon_equiped.min_atk - new_weapon.min_atk
            new_max_attack = weapon_equiped.max_atk - new_weapon.max_atk
            self.min_atk += new_min_attack
            self.max_atk += new_max_attack
        elif isinstance(weapon_equiped, Jewel):
            new_hp = weapon_equiped.hp - new_weapon.hp
            new_mp = weapon_equiped.mp - new_weapon.mp
            self.max_hp += new_hp
            self.mp += new_mp
        else:
            new_hp = weapon_equiped.hp - new_weapon.hp
            new_armor = weapon_equiped.armor - new_weapon.armor
            self.max_hp += new_hp
            self.armor += new_armor

