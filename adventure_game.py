import time
import random

global CaveVisitCounter 
CaveVisitCounter = 0



#Text Delay
def delay():
    time.sleep(0)

def initMonster():
    monsters = ['Dragon','Gorgon','Dog','Snake','Troll']
    monster = random.choice(monsters)
    return monster

global monster
monster = initMonster()

# User Response
def userChoice(choicea,choiceb):
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

def HouseOrCave():
    #choicea = House()
    #choiceb = Cave()
    choice = userChoice("house","cave")
    if choice == "house":
        House()
    elif choice == "cave":
        Cave()

def FightOrRunAway():
    #choicea = House()
    #choiceb = Cave()
    choice = userChoice("fight","runaway")
    if choice == "fight":
        # Check Cave Visit Counter
        #If sword win
        #If dagger lose
    elif choice == "runaway":
        # return to field 
        



def House():
    global monster
    print("You approach the door of house.")
    delay()
    print(f"You knock the door and steps out {monster} .")
    delay()
    print(f"This is {monster}'s house' .")
    delay()
    print("Would you like to (1) fight or (2) run away? ")
    return ""


def Cave():
    global CaveVisitCounter
    print("You peer cautiously into the cave.")
    delay()
    if CaveVisitCounter > 0 :
        print("You've been here and have all the stuff. It's empty now")
    else :
        print("It is a very small cave.")
        delay()
        print("You see a rock")
        delay()
        print("You found the magical Sword of Ilyoon!")
        delay()
        print("You discard your old dagger and take the sword with you")
        delay()
        print("You walkback out to the field")
        CaveVisitCounter= +1




#print(monster)
#Cave()
#Cave()
HouseOrCave()


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