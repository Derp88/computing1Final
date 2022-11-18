#This is a multipurpose file that allows other parts of the program to interact with the database

import sqlite3
#DB Connection
db = sqlite3.connect("computing1Final/main.db") #The file path shouldn't be stated normally, but it is required for python anywhere to work

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
        matchResultsRaw = cur.execute("SELECT * FROM matches WHERE matchNumber = ? AND teamNumber = ?", (matchNumber, teamNumber))
        matchResults = matchResultsRaw.fetchone()

        #Close the cursor
        cur.close()
        #Return the match results
        return matchResults

    #Get all match data
    def returnAllData(self):
        #Create the cursor
        cur = db.cursor()
        #View match results
        matchResultsRaw = cur.execute("SELECT * FROM matches")
        matchResults = matchResultsRaw.fetchall()
        #Close the cursor
        cur.close()
        #Return the match results
        return matchResults

    #Get all matches
    def returnMatches(self):
        #Create the cursor
        cur = db.cursor()
        #Gets all matches
        matchesRaw = cur.execute("SELECT matchNumber FROM matches")
        matchesUnsorted = matchesRaw.fetchall()
        matches = []
        #Close the cursor
        cur.close()
        #Remove duplicates
        for unsortedMatch in matchesUnsorted:
            #While doing this we can make the tuple(of one element) into a string
            AddMatch = "".join(str(unsortedMatch))
            AddMatch = AddMatch[1:][:-2]
            if AddMatch not in matches:
                matches.append(AddMatch)
        matches = matches.sort()
        return matches

    #Get all teams
    def returnTeams(self):
        #Create the cursor
        cur = db.cursor()
        #Gets all teams
        teamsRaw = cur.execute("SELECT teamNumber FROM matches")
        teamsUnsorted = teamsRaw.fetchall()
        teams = []
        #Close the cursor
        cur.close()
        #Remove duplicates
        for unsortedTeam in teamsUnsorted:
            #While doing this we can make the tuple(of one element) into a string
            AddTeam = "".join(str(unsortedTeam))
            #Adds team with uneeded parentheses and comma removed
            AddTeam = AddTeam[1:][:-2]
            if AddTeam not in teams:
                teams.append(AddTeam)
        teams = teams.sort()
        return teams

def main():
    database_io = db_interactor()
    #This is to add test data
    #database_io.setMatchData(1, 292, 1, 1, 3, 5, 0, 2)
    #print(database_io.returnTeamMatchData(1,292))
    print(database_io.returnMatches())
    print(database_io.returnTeams())


if __name__ == "__main__":
    main()