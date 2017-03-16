import sys
import os
import csv

# create main method
#import csv file
with open('soccer_players.csv', newline='') as csvfile:
    testreader = csv.DictReader(csvfile, delimiter='|')
    rows = list(testreader)
#import information into formatable code
#divide teams equally into three "sharks" "raptors" and "dragons"
#divide experienced players into three teams equally.  There are 9
#create a 'teams.txt' file theat includes name of team and each player on each team
#in the list of teams include, team name on one line, each player with their experience and 
#guardian names on a seperate line seperated by commas.
