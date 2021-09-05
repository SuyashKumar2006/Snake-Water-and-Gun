# importing "random"  module.
import random

print("Snake Water and Gun!")
print("Welcome to our Automated Gaming Program...")
print("The rules of our game is very simple")
def  gameInstructions():
    """This function is used for accessing the rules of the game."""
    print("Snake and Water, Snake wins")
    print("Snake and Gun, Gun wins")
    print("Gun and Water, Water wins")
    print("At any point of the game press 'E' to view the instructions ")

print("Kindly Follow the Instruction of the game:")
gameInstructions()

infinity = 1
playerScore = 0
computerScore = 0

while(infinity>0):




    userInput = input("Enter 'G' for Gun , 'S' for Snake , and 'W' for Water")
    if(userInput.lower()=="g"):
        print("Player's Choice: Gun")
        computerChoice = random.choice(["Water","Gun","Snake"])

        if(computerChoice.lower()=="snake"):
            playerScore +=1
            print("Computer's Choice:",computerChoice)
            print("You Won!")
        elif(computerChoice.lower()=="gun"):
            print("Computer's Choice:",computerChoice)
            print("It's a draw")
        else:
            computerScore +=1
            print("Computer's Choice:",computerChoice)
            print("You Lose")
        infinity += 1

        print("Player's Score:", playerScore)
        print("Computer's Score:", computerScore)
        print("Number of Rounds Left:",11-infinity)

    elif(userInput.lower()=="w"):
        print("You choosed Water")
        computerChoice = random.choice(["Water","Gun","Snake"])
        infinity+=1
        if (computerChoice.lower() == "gun"):
            playerScore += 1
            print("Computer's Choice:", computerChoice)
            print("You Won!")
        elif (computerChoice.lower() == "water"):
            print("Computer's Choice:", computerChoice)
            print("It's a draw")
        else:
            computerScore += 1
            print("Computer's Choice:", computerChoice)
            print("You Lose")

        print("Player's Score:", playerScore)
        print("Computer's Score:", computerScore)
        print("Number of Rounds Left:",11-infinity)
    elif(userInput.lower()=="s"):
        print("You choosed Snake")
        computerChoice = random.choice(["Water","Gun","Snake"])
        if (computerChoice.lower() == "water"):
            playerScore += 1
            print("Computer's Choice:", computerChoice)
            print("You Won!")
        elif (computerChoice.lower() == "snake"):
            print("Computer's Choice:", computerChoice)
            print("It's a draw")
        else:
            computerScore += 1
            print("Computer's Choice:", computerChoice)
            print("You Lose")
        infinity+=1
        print("Player's Score:", playerScore)
        print("Computer's Score:", computerScore)
        print("Number of Rounds Left:",11-infinity)

    elif(userInput.lower()=="e"):
        gameInstructions()
        print("Number of Rounds Left:",11-infinity)
        continue

    if(infinity==11):
        print("The Game is Finished. Calculating the results....")
        if(playerScore>computerScore):
            print("Congrats! You Won ;)")
            newGame= int(input("Enter 0 for a new game or 1 to exit:"))
            if(newGame==0):
                infinity=1
                playerScore=0
                computerScore=0
            else:
                break
        elif(playerScore==computerScore):
            print("It's a draw! T-T")

            newGame= int(input("Enter 0 for a new game or 1 to exit:"))

            if(newGame==0):
                infinity=1
                playerScore=0
                computerScore=0
            else:
                break
        elif(playerScore<computerScore):
            print("Alas! The Computer Won ;(")

            newGame= int(input("Enter 0 for a new game or 1 to exit:"))

            if(newGame==0):
                infinity=1
                playerScore=0
                computerScore=0
            else:
                break


print("Thank You! If you found any bug in the program please report at suyash.subhash@gmail.com")