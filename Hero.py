# coding=utf-8
from Character import *



class Hero(Character):
    #hero constructor defining all basic stats without equipements
    def __init__(self):
        Character.__init__(self)
        self.name = ""
        self.className = ""
        self.heroLevel = 1
        self.nextLevelXP = 1
        self.XP = 0
        self.HP = 50
        self.maxHP = 50
        self.MP = 100
        self.minDamage = 5
        self.maxDamage = 10
        self.armor = 5
        self.number_of_hp_pots = 1
        self.number_of_mp_pots = 1
        self.restLeft = 1
        self.inventory.equipement.first_stuff(self.heroLevel)
        self.stats_improve_from_stuff()
        self.potionUsed = 0
        self.mobKilled = 0

    #Setters to changer properly the value of an attributes
    def setHp(self):
        self.HP = self.maxHP

    def setName(self, name):
        self.name = name

    def setClass(self, classe):
        if classe == 1:
            self.className = "Naruto Runner"
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print("You're a professionel in naruto running, your goal is to pearce the defense of the zone 51")
            print("         Use your shuriken and run with your arms in the back floating in the air !")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
        elif classe == 2:
            self.className = "Berzerk"
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("You're the strongest class you have to contain the offensive of the zone 51")
            print("     Use your big belly to protect the stone thrower behind you !")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")
        elif classe == 3:
            self.className = "Stone Thrower"
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("You're the worst class unfortunately you choose the skinny one who just throw little stone...")
            print("                                 Try to not die...")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")
        else:
            self.className = "noob"
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("You are not able to choose between 1, 2 or 3, so for the rest of the adventure you'are a fucking noob")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")

    #Getters to acces specific attributes
    def get_hp(self):
        return self.HP

    def get_lvl(self):
        return self.heroLevel


    #Display all the hero informations
    def displayStat(self):
        print("#   #    #   #   #   #   #   #   #    #   #   #   #  ")
        print("| Name : " + str(self.name) + " | Class : " + str(self.className) + " | Level : " + str(self.heroLevel) + " |")
        print("| HP : " + str(self.HP) + "/" + str(self.maxHP) + " | MP : " + str(self.MP) + " | Armor : " + str(self.armor) + " |")
        print("| Damage Range : " + str(self.minDamage) + " - " + str(self.maxDamage) + " |")
        print("| Next level XP needed : " + str(self.nextLevelXP) + " | Actual XP : " + str(self.XP) + " |")
        print("| HP potion : " + str(self.number_of_hp_pots) + " | MP potion : " + str(self.number_of_mp_pots) + " |")
        print("| Gold : " + str(self.inventory.getGold()) + " |")
        print("#   #    #   #   #   #   #   #   #    #   #   #   #  ")


    #Display the 3 skills available
    def display_skill_available(self):
        print("             You have 3 different skill :                ")
        print(" (1) skill 1 : Deal hight damage to an enemy : cost 20 MP")
        print(" (2) skill 2 : Give back 20% of hero's life  : cost 30 MP")
        print(" (3) skill 3 : Reduce enemy's attack by 25%  : cost 20 MP")

    #Check if a spell can be cast depending on the MP available
    def mana_available_check(self, spell):
        if spell == 1:
            if self.MP >= 20:
                return True
            else:
                return False
        elif spell == 2:
            if self.MP >= 30:
                return True
            else:
                False
        elif spell == 3:
            if self.MP >= 15:
                return True
            else:
                return False

    #Change hero stats by adding the bonus stats from equipements to hero stats
    def stats_improve_from_stuff(self):
        if self.HP == 50:
            self.HP = self.maxHP
        self.maxHP += self.inventory.equipement.stuff_HP()
        self.HP += self.inventory.equipement.stuff_HP()
        self.MP += self.inventory.equipement.stuff_MP()
        self.minDamage += self.inventory.equipement.stuff_min_damage()
        self.maxDamage += self.inventory.equipement.stuff_max_damage()
        self.armor += self.inventory.equipement.stuff_armor()

    #Improve the hero stats after he level up by augmenting his previous stats
    def stats_improve_from_level_up(self):
        self.maxHP += 2 * self.heroLevel
        self.HP = self.maxHP #fully healed
        self.MP += 2 * self.heroLevel
        self.minDamage += 2 * self.heroLevel
        self.maxDamage += 2 * self.heroLevel
        self.armor += 2*self.heroLevel

    #check if the player have enought xp to reach an other level
    def check_for_level_up(self):
        while self.XP >= self.nextLevelXP:
            self.heroLevel += 1
            self.MP += 10
            self.XP -= self.nextLevelXP
            self.nextLevelXP += 2
            self.stats_improve_from_level_up()
            print("#####################")
            print("   YOU LEVEL UP !!!  ")
            print("#####################")

    #basic attack that inflict normal damage
    def basic_attack(self, enemy):
        damage = randint(self.minDamage, self.maxDamage)
        print("You hit the enemy and deal : "+ str(damage) + " damages.")
        enemy.attack_enemy(damage)

    #permit the player to receive damage form enemies
    def receive_damage(self, value):
        self.HP -= value

    def magic_skill_1(self, enemy): #Like the basic attack, but strongest
        damage = 2 * (randint(self.minDamage, self.maxDamage))
        print("You strongly hit the enemy and deal :" + str(damage) + " damages.")
        enemy.attack_enemy(damage)
        self.MP -= 20

    # Give back 20% of the hero max HP
    def magic_skill_2(self):
        heal = self.maxHP * 0.20
        if self.HP + heal >= self.maxHP:
            print("You are fully healed !")
            self.HP = self.maxHP
        else:
            print("After your healing incantation ou have now : " + str(self.HP) + " HP")
            self.HP += heal
        self.MP -= 30

    # Reduce the monster attack by 20%
    def magic_skill_3(self, enemy):
        value = 2 * self.heroLevel
        enemy.reduce_enemy_attack(value)
        self.MP -= 20

    #Present the equipement available in the inventory and the one equiped
    #The result of this fonction depend on the peace of equipment store in the inventory
    def change_equipement(self):
        loot = self.inventory.equipement.loot
        weapon = self.inventory.equipement.weapon
        jewel = self.inventory.equipement.jewel
        head = self.inventory.equipement.head
        chest = self.inventory.equipement.chest
        legs = self.inventory.equipement.legs
        shoes = self.inventory.equipement.shoes
        self.displayStat()
        print("There are", len(loot), "peace of equipment in your inventory, let's take a look at it :")
        for i in range(len(loot)):
            item = loot[i]
            if isinstance(loot[i], Weapon):
                print("Object " + str(i + 1) + " : Weapon ")
                print("Weapon equiped : ")
                weapon.show_stat_object()
                print("Weapon from the inventory : ")
                item.show_stat_object()
                choice = self.armor_change()
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
                choice = self.armor_change()
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
                choice = self.armor_change()
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
                choice = self.armor_change()
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
                choice = self.armor_change()
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
                choice = self.armor_change()
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

    #Ask the player if he wants to change or not a peace of stuff
    def armor_change(self):
        print("Do you want to trade equipment 1 for equipement 2 ? ")
        print(" (1) Yes")
        print(" (2) No ")
        print("----------------------------------------------------")
        while True:
            choice = input(">> ")
            try:
                if int(choice) == 1:
                    return 1
                elif int(choice) == 2:
                    return 2

                else:
                    print("Please enter a correct value !")

            except ValueError:
                print("Please enter a correct value !")

    #Permit to change 2 peace of stuff and update the stats of the hero
    #Display also the new stats after change occured
    def swap_stuff(self, stuff_equiped, stuff_from_inventory):
        print("You succesfully change your're stuff")
        tempo = stuff_equiped
        stuff_equiped = stuff_from_inventory
        stuff_from_inventory = tempo
        self.displayStat()
        if isinstance(stuff_equiped, Weapon):
            new_min_damage = stuff_equiped.minDamage - stuff_from_inventory.minDamage
            new_max_damage = stuff_equiped.maxDamage - stuff_from_inventory.maxDamage
            self.minDamage += new_min_damage
            self.maxDamage += new_max_damage
        elif isinstance(stuff_equiped, Jewel):
            new_HP = stuff_equiped.bonusHP - stuff_from_inventory.bonusHP
            new_MP = stuff_equiped.bonusMP - stuff_from_inventory.bonusHP
            self.maxHP += new_HP
            self.MP += new_MP
        else:
            new_HP = stuff_equiped.bonusHP - stuff_from_inventory.bonusHP
            new_armor = stuff_equiped.bonusArmor - stuff_from_inventory.bonusArmor
            self.maxHP += new_HP
            self.armor += new_armor
        print("Your new stats are :")
        self.displayStat()

