import random

print("Number Guessing Game")

preSetNum = random.randint(1, 9)
chances = 5

while chances > 0:
    numGuess = int(input("Guess A Number (Between 1-9): "))
    if numGuess == preSetNum:
        print("You Guessed the Correct Number!\n You Win")
        break
    elif numGuess < preSetNum:
        chances -= 1
        print(f"Your Guess Was Too Low\n Chances Left: {chances}")
        
    elif numGuess > preSetNum:
        chances -= 1
        print(f"Your Guess Was Too High\n ChancesLeft: {chances}")
    
    if chances == 3:
        print("Hint:")
        if preSetNum >= 5:
            print("The Number is Atleast 5")
        else:
            print("The Number is Less Than 5")

            
if chances == 0:
    print(f"You Lose\n The Number Was: {preSetNum}")
