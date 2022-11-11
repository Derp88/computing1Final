#This is a multipurpose file that allows other parts of the program to interact with the database

import sqlite3
#DB Connection
db = sqlite3.connect("main.db")

#Create DB insert class
class db_interactor(object):
    #Constructor 
    def __init__(self):
        object.__init__(self)
    
    #Set the match data
    def setMatchData(self, matchNumber, teamNumber, autoLowScore, autoHighScore, movedOffLine, teleLowScore, teleHighScore, climbBarSpot):
        #Create the cursor
        cur = db.cursor()
        #Insert match data into DB
        cur.execute("INSERT INTO matches VALUES(null, ?, ?, ?, ?, ?, ?, ?, ?)",(matchNumber, teamNumber, autoLowScore, autoHighScore, movedOffLine, teleLowScore, teleHighScore, climbBarSpot))
        db.commit()
        #Close the cursor
        cur.close()
    
    #Get match data for a individual team
    def returnTeamMatchData(self, matchNumber, teamNumber):
        #Create the cursor
        cur = db.cursor()
        #View match results
        matchResults = cur.execute("SELECT * FROM matches WHERE matchNumber = ? AND teamNumber = ?", (matchNumber, teamNumber))

        #Close the cursor
        cur.close()


def main():
    database_io = db_interactor()
    #This is to add test data
    #database_io.setMatchData(292, 1, 1, 1, 3, 5, 0, 2)
    database_io.returnTeamMatchData(11,1741)


if __name__ == "__main__":
    main()