#In this game, Basically 10 question will be asked to the player if the player answer correcty
#  it will be awarded by a point 

print("Welcome to our QUIZ Game!!!!")

Confirmation=input("Do you want to Play this Quiz?.\n Reply Yes or No \n")

if Confirmation.lower()=="yes" or Confirmation.lower()=="no":
    if Confirmation.lower() != "yes":
        print("Thanks for Coming! :)")
        quit()
else:
    print("Please reply properly!")

PName = input("Enter your Name:")
print(PName,"\n Let's Play:")
Score=0

Answer = input("What Does CPU stands for? \n")
if Answer == "central processing unit":
    print("Correct! :)")
    Score += 1
else:
    print("InCorrect! :(")

Answer = input("Computer is which type of Device? \n")
if Answer == "electronic":
    print("Correct! :)")
    Score += 1
else:
    print("InCorrect! :(")

Answer = input("What is the Full Form of RAM? \n")
if Answer == "random access memory":
    print("Correct! :)")
    Score += 1
else:
    print("InCorrect! :(")

Answer = input("Where is data Stored in a computer? \n")
if Answer == "CPU":
    print("Correct! :)")
    Score += 1
else:
    print("InCorrect! :(")

Answer = input("What is that input device used to type text and numbers on a document in the computer system \n")
if Answer == "keyboard":
    print("Correct! :)")
    Score += 1
else:
    print("InCorrect! :(")

Answer = input("Name the computer part that helps a user to hear information from the system \n")
if Answer == "speaker":
    print("Correct! :)")
    Score += 1
else:
    print("InCorrect! :(")

Answer = input("RAM is which type of memory? \n")
if Answer == "volatile":
    print("Correct! :)")
    Score += 1
else:
    print("InCorrect! :(")

Answer = input("What does ROM stand for? \n")
if Answer == "read only memory":
    print("Correct! :)")
    Score += 1
else:
    print("InCorrect! :(")

Answer = input("_____________ is an output device that displays information on the computer screen? \n")
if Answer == "monitor":
    print("Correct! :)")
    Score += 1
else:
    print("InCorrect! :(")

Answer = input("Which is the input device that allows a user to move the cursor or pointer on the screen? \n")
if Answer == "mouse":
    print("Correct! :)")
    Score += 1
else:
    print("InCorrect! :(")

print(PName,"you scored\n",Score)
