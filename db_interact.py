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
    
    #Get data for ID
    def returnIdData(self, ID):
        #Create the cursor
        cur = db.cursor()
        idResultsRaw = cur.execute("SELECT * FROM matches WHERE id = ?", (ID,))
        idResults = idResultsRaw.fetchone()
        #Close the cursor
        cur.close()
        return idResults

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

    #Gets all data for a team
    def returnTeamData(self, teamNumber):
        #Create the cursor
        cur = db.cursor()
        #View match results
        matchResultsRaw = cur.execute("SELECT * FROM matches WHERE teamNumber = ?", (teamNumber,))
        matchResults = matchResultsRaw.fetchall()

        #Close the cursor
        cur.close()
        #Return the match results
        return matchResults

    #Gets all data for a match
    def returnMatchData(self, matchNumber):
        #Create the cursor
        cur = db.cursor()
        #View match results
        matchResultsRaw = cur.execute("SELECT * FROM matches WHERE matchNumber = ?", (matchNumber,))
        matchResults = matchResultsRaw.fetchall()

        #Close the cursor
        cur.close()
        #Return the match results
        return matchResults

    #Get all data
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
            AddMatch = int(AddMatch[1:][:-2])
            if AddMatch not in matches:
                matches.append(AddMatch)
        matches.sort()
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
            AddTeam = int(AddTeam[1:][:-2])
            if AddTeam not in teams:
                teams.append(AddTeam)
        teams.sort()
        return teams

    #Delete a record
    def deleteRecord(self, ID):
        #Create the cursor
        cur = db.cursor()
        #Deletes record
        cur.execute("DELETE FROM matches WHERE ID = ?", (ID,))
        db.commit()
        #Close the cursor
        cur.close()

    #Update a record
    def updateRecord(self, ID, matchNumber, teamNumber, autoLowScore, autoHighScore, movedOffLine, teleLowScore, teleHighScore, climbBarSpot):
        #We shouldn't have to do any checks to make sure the ID is valid, because the user can't select one out of range
        #Create the cursor
        cur = db.cursor()
        #Update data
        cur.execute("UPDATE matches SET matchNumber = ?, teamNumber = ?, autoLowScore = ?, autoHighScore = ?, movedOffLine = ?, teleLowScore = ?, teleHighScore = ?, climbBarSpot = ? WHERE id = ?", 
        (matchNumber, teamNumber, autoLowScore, autoHighScore, movedOffLine, teleLowScore, teleHighScore, climbBarSpot, ID))
        db.commit()
        #Close the cursor
        cur.close()

def main():
    database_io = db_interactor()
    #This is to add test data
    #database_io.setMatchData(8, 292, 3, 3, 7, 8, 4, 2)
    #print(database_io.returnTeamMatchData(1,292))
    print(database_io.returnIdData(1))
    
    
    

if __name__ == "__main__":
    main()