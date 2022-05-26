#this is a  similar game like stone, paper and scissors
import random

def game(ComputersChoice,UserChoice):
    if ComputersChoice == UserChoice:
        return "Both choose the Same."
    elif ComputersChoice == 'S':
        if UserChoice == 'W':
            return "Computer Wins"
        else: 
            return "Player Wins"
    elif ComputersChoice == 'W':
        if UserChoice == 'S':
            return "Player Wins"
        else: 
            return "Computer  Wins"
    
    elif ComputersChoice == 'G':
        if UserChoice == 'S':
            return "Computer Wins"
        else: 
            return "Player Wins"
Choice = ['G','W','S']
ComputersChoice = random.choice(Choice)
UserChoice = input("Enter your Choice: Snake(S) Water(W) or Gun(G) \n")
UserChoice = UserChoice.upper()
print("COMPUTER CHOOSE :",ComputersChoice)
print("USER CHOOSE :",UserChoice)
print(game(ComputersChoice, UserChoice))