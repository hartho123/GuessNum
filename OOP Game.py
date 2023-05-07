
from random import randint

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def PlayOrNot(self):
        while True:
            play = input("Do you want to play Guess The Number? (Y/N)\n")
            if play.upper() == "Y":
                break
            else:
                pass

    def Play(self, name):
        guessCount = 0
        randNum = randint(1, 100)
        x = True
        while x == True:
            guess = input("Try to guess the randomly generated number\n")
            if not str(guess):
                print("Invalid Entry - Try Again")
            elif guess == randNum:
                guessCount += 1
                x = False
            elif int(guess) > int(randNum):
                print("Your guess was higher than the Guessing Number")
            elif int(guess) < int(randNum):
                print("Your guess was lower than the Guessing Number")
        return(f"{name} Guessed the number {randNum} in {guessCount} guesses!")

def Name():
        while True:
            name = (input("Enter your name: ")).capitalize()
            if not str(name):
                print("Invalid name - Try Again")
            else:
                break

def Age():
    while True:
        age = input("\nEnter your age: ")
        if not int(age):
            print("Invalid Entry - Try Again")
        else:
            break

def Stat(name, age, guessCount):
        print(f"{name} (Age {age}) -- {guessCount} points")

name1 = Name()
age1 = Age()


player1 = Player(name1, age1)
player1.PlayOrNot()
player1.Play(name1)











    

    
