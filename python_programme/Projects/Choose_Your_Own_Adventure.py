name=input("Enter your Name \n")
print("Welcome",name,"to this Adventure!")

answer = input(
    "You are on a dirt road, it has to come to an end you can go left or right,Which way you like to go?").lower()

if answer == 'left':
    answer = input("You come to a river,you can walk aroung or swim a river?,choose walk or swim!").lower()
    if answer == 'walk':
        print("You walk for many miles and ran out of water and you lose")
    elif answer == 'swim':
        print("you swim across and eaten by the alligater")
    else:
        print("Not a valid option.you lose")
        quit()
elif answer == 'right':
    answer=input("you come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back?)").lower()
    if answer == 'back':
        print("You go back and you lose")
    elif answer == 'cross':
        print("you cross the bridge and found the treasue")
    else:
        print("Not a valid option.you lose")
        quit()
else:
    print("Not a valid option.you lose")
    quit()