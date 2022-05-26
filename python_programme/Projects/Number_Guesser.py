import random

try:
    MRange = int(input("Enter number till you want to guess\n"))
except:
    print("Enter Only Number !!")
    quit()
if MRange <= 0:
    print("Next Time! Enter number greater than 0")
    quit()

RandomNumber = random.randint(0, MRange)
print(RandomNumber)
guesses =0
while True:
    guesses += 1
    try:
        UserChoice = int(input("Make a Guess: \n"))
    except:
        print("Enter Only Number !!")
        continue
    if UserChoice == RandomNumber:
        print("Correct! you Got it")
        break
    elif UserChoice > RandomNumber:
        print("InCorrect!\n You're above the number")
    else:
        print("InCorrect!\n You're below the number")
print("You Got it in",guesses,"Guesses")