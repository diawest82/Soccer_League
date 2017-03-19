import csv
import random

with open('soccer_players.csv', newline= '') as csvfile:
    testreader = csv.DictReader(csvfile, delimiter='|')
    rows = tuple(testreader)
    
#variables
exp =[]
no_exp = []
sharks = []
raptors = []
dragons = []


#seperate experience from no exp
def sep():
    for row in rows:
        for r in row.values():
            kn,ht,ex,gn = str(r).split(',')
            if 'YES' in ex:
                exp.append(''.join(i for i in str(r).replace(',','',1).replace(',', ', ') if i.isalpha() or i == ',' or i == ' '))
    
            if 'NO' in ex:
                no_exp.append(''.join(i for i in str(r).replace(',','',1).replace(',', ', ') if i.isalpha() or i == ',' or i == ' '))
                
    return exp, no_exp
        

#divides teams randomly from each list with exp and no exp split evenly
def divide_team():
    s,s2,s3,r,r2,r3,d,d2,d3 = random.sample(exp,9)
    s4,s5,s6,r4,r5,r6,d4,d5,d6 = random.sample(no_exp, 9)
    sharks.append(s), sharks.append(s2), sharks.append(s3),sharks.append(s4),sharks.append(s5),sharks.append(s6)
    raptors.append(r), raptors.append(r2),raptors.append(r3),raptors.append(r4),raptors.append(r5),raptors.append(r6)
    dragons.append(d), dragons.append(d2), dragons.append(d3),dragons.append(d4),dragons.append(d5),dragons.append(d6)
    return sharks, dragons, raptors, d


#divide the teams up evenly
def shark(team):
    #print teams to list
    team = team
    with open('teams.txt', 'a') as file:
        file.write('Team Sharks\n')
        for t in team:
            file.write(t+'\n')
        file.write('\n\n\n\n')
        
def dragon(team):
    team = team
    with open('teams.txt', 'a') as file:
        file.write('Team Dragons\n')
        for t in team:
            file.write(t+'\n')
        file.write('\n\n\n\n')

def raptor(team):
    team = team
    with open('teams.txt', 'a') as file:
        file.write('Team Raptors\n')
        for t in team:
            file.write(t+'\n')
        file.write('\n\n\n\n')


#welcome letters for each team
def shark_welcome(team):
    team = team
    for s in team:
        kn,ex,gn = s.split(',')
        with open('{}.txt'.format(kn).replace(' ', '_').lower(), 'a') as file:
            file.write('Dear{},\n\n'.format(gn))
            file.write('We are very excited this year to have {} on team Sharks!  We will'
                        ' have our first practice next Monday at 7:00 pm at field 2.  '
                        'Please make sure that you bring their equipment and something to drink.'.format(kn))


def raptor_welcome(team):
    team = team
    for s in team:
        kn,ex,gn = s.split(',')
        with open('{}.txt'.format(kn).replace(' ', '_').lower(), 'a') as file:
            file.write('Dear{},\n\n'.format(gn))
            file.write('We are very excited this year to have {} on team Raptors!  We will'
                        ' have our first practice next Monday at 7:00 pm at field 3.  '
                        'Please make sure that you bring their equipment and something to drink.'.format(kn))


def dragon_welcome(team):
    team = team
    for s in team:
        kn,ex,gn = s.split(',')
        with open('{}.txt'.format(kn).replace(' ', '_').lower(), 'a') as file:
            file.write('Dear{},\n\n'.format(gn))
            file.write('We are very excited this year to have {} on team Dragons!  We will'
                        ' have our first practice next Monday at 7:30 pm at field 1.  '
                        'Please make sure that you bring their equipment and something to drink.'.format(kn))
            
#execute the list
def main():
    sep()
    divide_team()
    raptor(raptors)
    shark(sharks)
    dragon(dragons)  
    shark_welcome(sharks)
    raptor_welcome(raptors)
    dragon_welcome(dragons)



if __name__=='__main__':
    main()

        
        
