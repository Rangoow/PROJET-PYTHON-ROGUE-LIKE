import sqlite3

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
    bdd.commit()

def insertData(name, classname, level, room, game_finished):
    bdd = sqlite3.connect('DataBase_Rogue_Like.db')
    cursor = bdd.cursor()
    cursor.execute("""
    INSERT INTO player(name, class, level, room, game_finished) VALUES(?, ?, ?, ?, ?, ?)""",(name, classname, level, room, game_finished))
    bdd.commit()
    bdd.close()


