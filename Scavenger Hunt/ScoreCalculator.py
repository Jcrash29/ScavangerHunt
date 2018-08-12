# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import re
from collections import Counter


# Get our current location

List = []

TeamNames = []
TeamScores = []


def addToScore(inputName):
    i = 0
    FoundTeam = False
    for teamName in TeamNames:
        if inputName == teamName:
            TeamScores[i] += 1
            FoundTeam = True
            break
        i += 1
    if FoundTeam == False:
        TeamNames.append(inputName)
        TeamScores.append(1)


def printScores():
    with open ('Scores.txt', 'wr') as file:
        i = 0
        for teamName in TeamNames:
            print teamName + '    ' + str(TeamScores[i]) + '\r\n'
            file.write(teamName + '    ' + str(TeamScores[i]) + '\r\n') 
            i += 1

def mainStuff(exDir):
    # Navigate through each of the 
    for dir in os.listdir(exDir):
        #We can exclude any directories here.
        if(os.path.isfile(os.path.join(exDir,dir)) == False):
            #print exDir + '/' + dir + ':'
            location = exDir + '/' + dir
            for file in os.listdir(location):
                #print file
                teamName = file.split('.',1)[0]
                List.append(teamName)
                addToScore(teamName)
#print Counter(List)
#print List
    printScores()
            
if __name__=='__main__':
    exDir = os.getcwd()
    mainStuff(exDir)



    
    
