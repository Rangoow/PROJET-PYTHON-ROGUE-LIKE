import sqlite3
#Create a database to store success and player information
#2 different table on for player the other for achievements
def createDB():
    bdd = sqlite3.connect('DataBase_Rogue_Like.db')
    cursor = bdd.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS player(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         name TEXT,
         class TEXT,
         level INTERGER,
         room INTEGER,
         game_finished TEXT
    )
    """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS achievements(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        player_name TEXT,
        name TEXT,
        desc TEXT,
        val TEXT
    )""")
    bdd.commit()


#Inser data into the table player
def insertData(name, classname, level, room, game_finished):
    bdd = sqlite3.connect('DataBase_Rogue_Like.db')
    cursor = bdd.cursor()
    cursor.execute("""
        INSERT INTO player(name, class, level, room, game_finished) VALUES(?, ?, ?, ?, ?)""",(name, classname, level, room, game_finished))
    bdd.commit()
    bdd.close()

#insert data into the achievements table
def insertAchievements(achievement, player):
    bdd = sqlite3.connect('DataBase_Rogue_Like.db')
    cursor = bdd.cursor()
    cursor.execute("""
       INSERT INTO achievements(player_name, name, desc, val) VALUES(?, ?, ?, ?)""",(player, achievement[0],achievement[1], achievement[2]))
    bdd.commit()
    bdd.close()