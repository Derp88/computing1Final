#The purpose of this program is to create a new empty database for the site.
import sqlite3
#DB Connection
db = sqlite3.connect("main.db")
cur = db.cursor()

def buildDB():
    #Creates a table with the specified items
    matchesTableSetup = """
    CREATE TABLE matches (
    id INTEGER PRIMARY KEY,
    matchNumber INTEGER,
    teamNumber INTEGER,
    autoLowScore INTEGER,
    autoHighScore INTEGER,
    movedOffLine INTEGER,
    teleLowScore INTEGER,
    teleHighScore INTEGER,
    climbBarSpot INTEGER
    )
    """
    cur.execute(matchesTableSetup)
    db.commit()

def main():
    buildDB()
    #Close connection to db
    cur.close()

if __name__ == "__main__":
    main()