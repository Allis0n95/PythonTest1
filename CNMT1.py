rolls = int(input ('How many times do you want to roll?'))
sides = int(input ('How many sides is your die?'))

import random

for rolls in range (rolls):
    randomDice = random.randrange(sides)+1
    print (randomDice)
    if randomDice==20:
        print('critical hit!')
    if randomDice==1:
        print('critical FAIL')
        
print ('done rolling')

#Link I used for help
#https://codehs.com/tutorial/rachel/user-input-in-python

#Github link
#https://github.com/Allis0n95/PythonTest1/blob/main/CNMT1.py
