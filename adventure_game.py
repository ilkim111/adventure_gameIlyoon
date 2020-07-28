import time
import random

global CaveVisitCounter
CaveVisitCounter = 0


# Text Delay
def delay():
    time.sleep(1)


def Prompt(message):
    print(message)
    delay()


def initMonster():
    monsters = ['Dragon', 'Gorgon', 'Dog', 'Snake', 'Troll']
    monster = random.choice(monsters)
    return monster


global monster
monster = initMonster()

# User Response


def userChoice(choicea, choiceb):
    answer = input("Please Enter 1 or 2:")
    while answer not in ('1', '2'):
        answer = input("Please Enter 1 or 2:")
    if answer in ('1', '2'):
        if answer == '1':
            return choicea
        if answer == '2':
            return choiceb

# Intro


def Intro():
    Prompt("You are in Wood")
    Prompt("You have dagger")
    Prompt("You see a house")
    Prompt("You see a cave")
    Prompt("")
    HouseOrCave()


def HouseOrCave():
    #choicea = House()
    #choiceb = Cave()
    Prompt("Enter 1 to get into house")
    Prompt("Enter 2 to enter cave")
    Prompt("What Would you like to do?")
    choice = userChoice("house", "cave")
    if choice == "house":
        House()
    elif choice == "cave":
        Cave()


def FightOrRunAway():
    #choicea = House()
    #choiceb = Cave()
    choice = userChoice("fight", "runaway")
    if choice == "fight":
        if CaveVisitCounter == 0:
            print("You Lose")
            PlayAgain()
        else:
            global monster
            Prompt(
                f"As the {monster} moves to attack you unsheath the new sword")
            Prompt(
                f"The sword shine brightly in your hand as you brace yourself for attack")
            Prompt(f"But {monster} is scared by your weapon and runs away")
            Prompt("You Win")
            PlayAgain()

        # Check Cave Visit Counter
        # If sword win
        # If dagger lose
    elif choice == "runaway":
        Prompt(f"You Choose to run away")
        HouseOrCave()
        # return to field


def PlayAgain():
    answer = input("Would you like to play again? (y/n)")
    while answer not in ('y', 'n'):
        answer = input("Would you like to play again? (y/n)")
    if answer in ('y', 'n'):
        if answer == 'y':
            Prompt("Restarting Game")
            Intro()
        if answer == 'n':
            Prompt("Okay Bye!")


def House():
    global monster
    Prompt("You approach the door of house.")
    Prompt(f"You knock the door and steps out {monster}.")
    Prompt(f"This is {monster}'s house.")
    Prompt(f"{monster} attacks you.")
    Prompt("Would you like to (1) fight or (2) run away? ")
    FightOrRunAway()


def Cave():
    global CaveVisitCounter534
    Prompt("You peer cautiously into the cave.")
    if CaveVisitCounter > 0:
        Prompt("You've been here and have all the stuff. It's empty now")
        Prompt("You walkback out to the field")
        HouseOrCave()
    else:
        Prompt("It is a very small cave.")
        Prompt("You see a rock")
        Prompt("You found the magical Sword of Ilyoon!")
        Prompt("You discard your old dagger and take the sword with you")
        Prompt("You walkback out to the field")
        CaveVisitCounter = +1
        HouseOrCave()


Intro()

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
