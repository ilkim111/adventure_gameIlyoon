import time
import random




#Text Delay
def delay():
    time.sleep(0)

def initMonster():
    monsters = ['Dragon','Gorgon','Dog','Snake','Troll']
    monster = random.choice(monsters)
    return monster


# User Response
def userChoice(choicea, choiceb):
    answer = input("Please Enter 1 or 2:")
    while answer not in ('1','2'):
        answer = input("Please Enter 1 or 2:")
    if answer in ('1','2'):
        if answer == '1':
            return choicea
        if answer == '2':
            return choiceb
            
# Intro 
def Intro():
    print("You are in Wood")
    delay()
    print("You have dagger")
    delay()
    print("You see a house")
    delay()
    print("You see a cave")
    delay()
    print("You have dagger")
    delay()
    print("")
    delay()
    print("Enter 1 to get into house")
    delay()
    print("Enter 2 to enter cave")
    delay()
    print("What Would you like to do?")
    delay()
    print(userChoice('house','cave'))

def House():
    return house


def Cave():
    if HouseVisitCounter > 0 :
        print("You All Ready Have the Weapon")
    else :
        print
    return cave


HouseVisitCounter = 0
monster = initMonster()

Intro()
print(monster)


'''
1. Print descriptions of what's happening for the player

2. Pausing between printing descriptions

3. Give the player some choices

4. Make sure the player gives a valid input

5. Add functions and refactor your code

6. Use randomness in your game

7. Create win and lose conditions

8. Check if the player wants to play again

9. Check your style with pycodestyle
'''