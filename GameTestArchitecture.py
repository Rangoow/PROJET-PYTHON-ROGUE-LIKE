from Hero import *
from Monster import *
import os
import sys
import random

class gameTestArchitecture:
    def __init__(self):
        self.level = 1
        self.hero = Hero()
        self.place = 0
        #Battle = 1 / Shop = 2 / Rest = 3
        self.room = [1,1,1,1,1]

    def display_game_title(self):
        self.disp_separator(36)
        print('¤ Welcome to the 51 Area Raid RPG! ¤')
        self.disp_separator(36)
        self.disp_blank(1)

    def disp_blank(self,n):
        print('\n'*n)

    def disp_separator(self,n):
        print('#'*n)

    def startGame(self):
        self.hero.setHp()
        self.display_game_title()
        print("What's your name ? ")
        tmp=input(">> ")
        self.hero.setName(tmp)
        print("What's your class ? ")
        self.disp_separator(21)
        print("  (1) Naruto Runner  ")
        print("  (2) Berzerk        ")
        print("  (3) Stone Thrower  ")
        self.disp_separator(21)
        test = 1
        while test == 1:
            try:
                tmp = input(">> ")
                if int(tmp) == 1 or int(tmp)== 2 or int(tmp)== 3:
                    self.hero.setClass(int(tmp))
                    test=0
                else:
                    print("Please enter a correct Value")
            except ValueError:
                print("Please enter a correct Value")
        self.hero.displayStat()
        self.gameLoop()

    def menu(self):
        print("")
        print("You are at level : ", self.level,'.')
        self.disp_separator(21)
        print("Choose an action : ")
        self.disp_separator(21)
        print("  (1) Continue       ")
        print("  (2) Character Info ")
        print("  (3) Exit Game      ")
        self.disp_separator(21)

    def gameLoop(self):
        if self.level == 5:
            self.room.append(2)
        elif self.level == 10:
            self.room.append(3)
        while self.game_state():
            self.menu()
            try:
                choice = input(">> ")
                if int(choice) == 1:
                    self.disp_blank(1)
                    self.adventure_continue()
                elif int(choice) == 2:
                    self.disp_blank(1)
                    self.hero.displayStat()
                elif int(choice) == 3:
                    print("Thanks for your participation !")
                    sys.exit()
                else:
                    print("Please enter a correct Value")
            except ValueError:
                print("Please enter a correct Value")

    def adventure_continue(self):
        while self.level != 20:
            if self.level % 3 != 0:
                self.random_action()
            else: #each 3 level offer the possibility to came back to main menu (and check info of hero or exit)
                self.level+=1
                break

    def random_action(self):
        tmp = random.choice(self.room)
        if int(tmp) == 1:
            self.disp_blank(1)
            self.random_battle()
        elif int(tmp) == 2:
            self.disp_blank(1)
            self.shop()
        elif int(tmp) == 3:
            self.disp_blank(1)
            self.rest()

    def random_battle(self):
        if self.level < 20:
            print("You encounter an evil CIA agent ! Let's fight against him")
            self.disp_separator(50)
        elif self.level >= 20:
            print("You are at the final, let's defeat Donald Trump and recover the Alien eggs !")
            self.disp_separator(69)
        self.battle()

    def battle(self):
        enemy = Monster()
        if self.level >= 20:
            enemy.generate_final_boss()
        else:
            enemy.generate_enemy(self.level)
        while self.hero.hp > 0 and enemy.hp > 0:
            self.disp_separator(16)
            print("Eneny has :" + str(enemy.hp) + "/" + str(enemy.max_hp))
            print("You have  :" + str(self.hero.hp) + "/" + str(self.hero.max_hp))
            self.disp_separator(16)
            self.disp_blank(1)
            pass_turn = True
            while pass_turn:
                print("Choose an action : ")
                self.disp_separator(21)
                print("   (1) Attack        ")
                print("   (2) Use a potion  ")
                print("   (3) Pass turn     ")
                self.disp_separator(21)
                choice = input(">> ")
                try:
                    if int(choice) == 1:
                        self.attack_possibility(enemy)
                        pass_turn = False
                    elif int(choice) == 2:
                        self.use_potion()
                    elif int(choice) == 3:
                        print("End of your turn")
                        pass_turn = False

                    else:
                        print("Please enter a correct Value")
                except ValueError:
                    print("Please enter a correct Value")

        if self.hero.hp > 0:
            print("Vous avez fini la salle numero ", self.level, ".")
            self.hero.check_for_level_up()
            print("Que voulez vous faire : ")
            self.hero.change_equipement()
            self.level += 1
            # Passer a la salle suivant/ regarder son inventaire.
            add_rest_chance = randint(1, 5)
            if add_rest_chance > 3:
                print("You aerned an additional rest ! ")
                self.hero.restLeft += 1

    def use_potion(self):
        self.disp_separator(14)
        print(" (1) HP Potion")
        print(" (2) MP Potion")
        print(" (3) Return   ")
        self.disp_separator(14)
        while True:
            choice = input(">> ")
            try:
                if int(choice) == 1 and self.hero.hp < self.hero.max_hp:
                    self.hero.hp += self.level*4
                    if self.hero.hp > self.hero.max_hp:
                        self.hero.hp = self.hero.max_hp
                    break
                elif int(choice) == 2:
                    self.hero.mp += 20
                    break
                elif int(choice) == 3:
                    break
                else:
                    print("Please enter a correct Value")
            except ValueError:
                print("Please enter a correct Value")

    def attack_possibility(self, enemy):
        while enemy.hp > 0 and self.hero.hp > 0:
            self.disp_separator(21)
            print("   (1) Basic Attack   ")
            print("   (2) Magic attack   ")
            print("   (3) Return         ")
            self.disp_separator(21)
            choice = input(">> ")
            try:
                if int(choice) == 1:
                    self.hero.basic_attack(enemy)
                    enemy.attack_hero(self.hero)
                    if enemy.check_enemy_state():
                        enemy.generate_loot(self.hero)
                elif int(choice) == 2:
                    self.hero.show_skill_in_book()
                    while True:
                        choice = input(">> ")
                        try:
                            if int(choice) == 1:
                                print("You choose spell 1 !")
                                if self.hero.mana_available_check(int(choice)):
                                    self.hero.magic_skill_1(enemy)
                                    if enemy.check_enemy_state():
                                        enemy.generate_loot(self.hero)
                                    break
                                else:
                                    self.disp_blank(1)
                                    print("Not enought mana to cast this spell")
                                    self.disp_blank(1)
                                    break
                            elif int(choice) == 2:
                                if self.hero.mana_available_check(int(choice)):
                                    print("You choose spell 2 !")
                                    self.hero.magic_skill_2()
                                    break
                                else:
                                    self.disp_blank(1)
                                    print("Not enought mana to cast this spell")
                                    self.disp_blank(1)
                                    break
                            elif int(choice) == 3:
                                if self.hero.mana_available_check(int(choice)):
                                    print("You choose spell 3 !")
                                    self.hero.magic_skill_3(enemy)
                                    break
                                else:
                                    self.disp_blank(1)
                                    print("Not enought mana to cast this spell")
                                    self.disp_blank(1)
                                    break
                            else:
                                print("Please enter a correct Value")
                        except ValueError:
                            print("Please enter a correct Value")
                elif int(choice) == 3:
                    break
                else:
                    print("Please enter a correct Value")
            except ValueError:
                print("Please enter a correct Value")

    def shop(self):
        self.disp_separator(21)
        print("¤       SHOP        ¤")
        self.disp_separator(21)
        hp_pot_price = 4
        mp_pot_price = 6
        self.disp_separator(21)
        print(" (1) Magic HP potion : " + str(hp_pot_price) + " gold.")
        print(" (1) Magic MP potion : " + str(mp_pot_price) + " gold.")
        print(" (3) No thanks !")
        self.disp_separator(21)
        print("Do you want to buy something ?")
        while True:
            choice = input(">> ")
            try:
                if int(choice) == 1:
                    if self.hero.inventory.getGold() >= hp_pot_price:
                        print("You bought a HP potion !")
                        self.hero.inventroy.gold -= hp_pot_price
                        self.hero.number_of_hp_pots += 1
                        break
                    else:
                        self.disp_blank(1)
                        print("Sorry but you don't have enought gold...")
                        self.disp_blank(1)
                        break
                elif int(choice) == 2:
                    if self.hero.inventory.getGold() >= mp_pot_price:
                        print("You bought a MP potion !")
                        self.hero.inventroy.gold -= mp_pot_price
                        self.hero.number_of_mp_pots += 1
                        break
                    else:
                        self.disp_blank(1)
                        print("Sorry but you don't have enought gold...")
                        self.disp_blank(1)
                        break
                elif int(choice) == 3:
                    break
                else:
                    print("Please enter a correct Value")
            except ValueError:
                print("Please enter a correct Value")

    def rest(self):
        if self.hero.restLeft >= 0:
            print("Do you want to take a rest ?")
            print(" (1) Yes, I'm tired !")
            print(" (2) No, I'm still ready to fight !")
            while True:
                choice = input(">> ")
                try:
                    if int(choice)==1 and self.hero.hp < self.hero.max_hp:
                        hprestored = randint(self.hero.lvl * 3,self.hero.lvl*5)
                        self.hero.hp += hprestored
                        if self.hero.hp > self.hero.max_hp:
                            self.hero.hp = self.hero.max_hp
                        self.disp_blank(1)
                        print("You took a 10 minutes break, you're now ready !")
                        print("You have now : " + str(self.hero.hp) + "/" + str(self.hero.max_hp) + "HP.")
                        self.disp_blank(1)
                        self.hero.restLeft -= 1
                        break
                    elif int(choice) == 2:
                        break
                    elif self.hero.hp > self.hero.max_hp:
                        print("You are full health, go fight !")
                    else:
                        print("Please enter a correct Value")
                except ValueError:
                    print("Please enter a correct Value")

    def game_state(self):
        if self.hero.hp < 0:
            self.disp_separator(35)
            print("Sorry but you are dead, try again !")
            self.disp_separator(35)
            self.disp_blank(2)
            return False
        elif self.level > 20:
            self.disp_separator(38)
            print("You finished the game, congratulations !")
            self.disp_separator(38)
            return False
        else:
            return True
