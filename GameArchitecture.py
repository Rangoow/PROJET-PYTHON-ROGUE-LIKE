from Hero import *
from Enemy import *
import os
import sys
import numpy as np
from DataBaseManagement import *
from Achievements import *

class gameArchitecture:
    def __init__(self):
        self.level = 1
        self.hero = Hero()
        self.place = 0
        #Battle = 1 / Shop = 2 / Rest = 3
        self.room = [1,1,1,1]
        #Change this value to change the duration of the game
        self.finalLevel = 30
        createDB()

    def display_game_title(self):
        self.disp_separator(36)
        print('¤ Welcome to the 51 Area Raid RPG! ¤')
        self.disp_separator(36)
        print("You have been call to join the most important mission of the XXIst century...")
        print("They called it : Storm Area 51, They can't stop all of us...")
        print("We are the 20th september and you're actually waiting for the attack start...")
        self.disp_blank(1)
        insertAchievements(achivements7,self.hero.name)
        print("¤  YOU EARNED AN ACHIEVEMENTS ! ¤")
        print("")

    def disp_blank(self,n):
        print('\n'*n)

    def disp_separator(self,n):
        print('#'*n)

    #Ask for basic information about the player class and name
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

    #display mainmenu
    def menu(self):
        print("")
        print("You are at level : " + str(self.level) +'.')
        self.disp_separator(21)
        print("Choose an action : ")
        self.disp_separator(21)
        print("  (1) Continue       ")
        print("  (2) Character Info ")
        print("  (3) Exit Game      ")
        self.disp_separator(21)

    #define main game loop choose between running the game of see character informations or exit the game
    def gameLoop(self):
        if self.level == 5:
            self.room.append(2)
        elif self.level == 10:
            self.room.append(3)
        while self.game_state():
            self.menu()
            print("Your HP are : " + str(self.hero.HP) + " / " + str(self.hero.maxHP))
            try:
                choice = input(">> ")
                if int(choice) == 1:
                    self.adventure_continue()
                elif int(choice) == 2:
                    self.hero.displayStat()
                elif int(choice) == 3:
                    print("Thanks for your participation !")
                    insertData(self.hero.name, self.hero.className, self.hero.heroLevel, self.level,"NO")
                    sys.exit()
                else:
                    print("Please enter a correct Value")
            except ValueError:
                print("Please enter a correct Value")

    #continue the game while final level not reach
    def adventure_continue(self):
        while self.level != self.finalLevel:
            self.random_action()
            break

    #randomize the contents of the room
    #Fight / Shop / Rest
    def random_action(self):
        tmp = np.random.choice(self.room)
        print(tmp)
        if int(tmp) == 1:
            self.disp_blank(1)
            self.random_battle()
        elif int(tmp) == 2:
            self.disp_blank(1)
            self.shop()
        elif int(tmp) == 3:
            self.disp_blank(1)
            self.rest()

    #Create a new battle
    #in case it's the final level, battle with the boss
    def random_battle(self):
        if self.level < self.finalLevel:
            print("You encounter an evil CIA agent ! Let's fight against him")
            self.disp_separator(50)
            self.battle()
        elif self.level >= self.finalLevel:
            print("Dear " + str(self.hero.className) + " you reached the las point of this adventure...")
            print("You are at the final, let's defeat Donald Trump and recover the Alien eggs !!")
            self.disp_separator(70)
            self.battle()

    #battle function that permit the player to attack ennemy / use potion or skip turn
    #in case it's the final level, battle with the boss
    def battle(self):
        enemy = Enemy()
        if self.level >= self.finalLevel:
            enemy.generate_final_boss()
        else:
            enemy.generate_enemy(self.level)
        while self.hero.HP > 0 and enemy.HP > 0:
            self.disp_separator(18)
            print("Enemy has : " + str(enemy.HP) + "/" + str(enemy.maxHP))
            print("You have  : " + str(self.hero.HP) + "/" + str(self.hero.maxHP))
            self.disp_separator(18)
            self.disp_blank(1)
            pass_turn = True
            while pass_turn:
                print("Your HP are : " + str(self.hero.HP) + " / " + str(self.hero.maxHP))
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
                        self.disp_separator(1)
                        enemy.attack_hero(self.hero)
                        pass_turn = False

                    else:
                        print("Please enter a correct Value")
                except ValueError:
                    print("Please enter a correct Value")

        if self.hero.HP > 0:
            print("You finished room ", self.level, ".")
            self.hero.check_for_level_up()
            print("INVENTORY CHECK")
            self.hero.change_equipement()
            self.level += 1
            add_rest_chance = randint(1, 5)
            if add_rest_chance > 3:
                print("You earned an additional rest ! ")
                self.hero.restLeft += 1
            if self.hero.mobKilled == 5:
                insertAchievements(achivements3,self.hero.name)
                print("¤  YOU EARNED AN ACHIEVEMENTS ! ¤")
            if self.hero.mobKilled == 10:
                insertAchievements(achivements4,self.hero.name)
                print("¤  YOU EARNED AN ACHIEVEMENTS ! ¤")

    #permit to use a potion of HP or MP
    def use_potion(self):
        self.disp_separator(14)
        print(" (1) HP Potion")
        print(" (2) MP Potion")
        print(" (3) Return   ")
        self.disp_separator(14)
        while True:
            choice = input(">> ")
            try:
                if int(choice) == 1 and self.hero.HP < self.hero.maxHP and self.hero.number_of_hp_pots > 0:
                    self.hero.HP += self.level * 4
                    if self.hero.HP > self.hero.maxHP:
                        self.hero.HP = self.hero.maxHP
                        print("     You recover some HP !")
                    self.hero.number_of_hp_pots -=1
                    self.hero.potionUsed +=1
                    if self.hero.potionUsed >=3 :
                        insertAchievements(achivements2,self.hero.name)
                        print("¤  YOU EARNED AN ACHIEVEMENTS ! ¤")
                    break
                elif int(choice) == 2 and self.hero.number_of_mp_pots > 0:
                    self.hero.MP += 20
                    print("     You recover 20 magic point !")
                    self.hero.number_of_mp_pots-=1
                    break
                elif int(choice) == 3:
                    break
                else:
                    print("You're fully healed cannot take a Potion or you don't have enought potion")
            except ValueError:
                print("Please enter a correct Value")

    #Permit to choose between basic or magic attack
    def attack_possibility(self, enemy):
        while enemy.HP > 0 and self.hero.HP > 0:
            self.disp_separator(21)
            print("   (1) Basic Attack   ")
            print("   (2) Magic attack   ")
            print("   (3) Return         ")
            self.disp_separator(21)
            choice = input(">> ")
            try:
                if int(choice) == 1:
                    self.hero.basic_attack(enemy)
                    if enemy.check_enemy_state():
                        enemy.generate_loot(self.hero)
                    enemy.attack_hero(self.hero)
                elif int(choice) == 2:
                    self.hero.display_skill_available()
                    while True:
                        choice = input(">> ")
                        try:
                            if int(choice) == 1:
                                print("You choose spell 1 !")
                                if self.hero.mana_available_check(int(choice)):
                                    self.hero.magic_skill_1(enemy)
                                    if enemy.check_enemy_state():
                                        enemy.generate_loot(self.hero)
                                    enemy.attack_hero(self.hero)
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

    #permit to buy potion to a shop against gold earned dring fight
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
                        insertAchievements(achivements1,self.hero.name)
                        print("¤  YOU EARNED AN ACHIEVEMENTS ! ¤")
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
        self.level += 1

    #Permit the player to take a rest and recover some health
    def rest(self):
        if self.hero.restLeft >= 0:
            print("Do you want to take a rest ?")
            print(" (1) Yes, I'm tired !")
            print(" (2) No, I'm still ready to fight !")
            while True:
                choice = input(">> ")
                try:
                    if int(choice) == 1 and self.hero.HP < self.hero.maxHP:
                        hprestored = randint(self.hero.heroLevel * 3, self.hero.heroLevel * 5)
                        self.hero.HP += hprestored
                        if self.hero.HP > self.hero.maxHP:
                            self.hero.HP = self.hero.maxHP
                        self.disp_blank(1)
                        print("You took a 10 minutes break, you're now ready !")
                        print("You have now : " + str(self.hero.HP) + "/" + str(self.hero.maxHP) + "HP.")
                        self.disp_blank(1)
                        self.hero.restLeft -= 1
                        break
                    elif int(choice) == 2:
                        break
                    elif self.hero.HP > self.hero.maxHP:
                        print("You are full health, go fight !")
                    else:
                        print("Please enter a correct Value")
                except ValueError:
                    print("Please enter a correct Value")
            self.level += 1

    #return the state of the game if he had to still run or not
    #If you die the game have to stop
    #if you kill the final boss the game have to stop
    #else it have to continue
    def game_state(self):
        createDB()
        if self.hero.HP < 0:
            self.disp_separator(35)
            print("Sorry but you are dead, try again !")
            insertAchievements(achivements6,self.hero.name)
            print("¤  YOU EARNED AN ACHIEVEMENTS ! ¤")
            insertData(self.hero.name, self.hero.className, self.hero.heroLevel, self.level, "No")
            self.disp_separator(35)
            self.disp_blank(2)
            return False
        elif self.level > self.finalLevel:
            self.disp_separator(38)
            print("You finished the game, congratulations !")
            insertAchievements(achivements5,self.hero.name)
            print("¤  YOU EARNED AN ACHIEVEMENTS ! ¤")
            insertData(self.hero.name, self.hero.className, self.hero.heroLevel, self.level, "Yes")
            self.disp_separator(38)
            return False
        else:
            return True
