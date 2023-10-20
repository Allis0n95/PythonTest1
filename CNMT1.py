rolls = int(input ('How many times do you want to roll?')) #asks for number of rolls
sides = int(input ('How many sides is your die?')) #asks for number of sides
#above is the roll and side integers

import random #makes sure the numbers are random

for rolls in range (rolls): #rolls dice based off of roll input number
    randomDice = random.randrange(sides)+1 #rolls dice/die with amount of sides as side input number
    print (randomDice) #shows dice/die roll numbers to screen
    if randomDice==20:
        print('critical hit!') #checks for critical hit (20) then outputs if true
    if randomDice==1:
        print('critical FAIL') #checks for critical fail (1) then outputs if true
        
print ('done rolling')
#will say when the code is done and that there will be no more rolls


#Link I used for help
#https://codehs.com/tutorial/rachel/user-input-in-python

#Github link
#https://github.com/Allis0n95/PythonTest1/blob/main/CNMT1.py
