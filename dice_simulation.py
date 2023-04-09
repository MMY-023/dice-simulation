import random

def dice():

    # Generate a randome number
    num = random.randint(1,6)

    print("""Rolling The Dice...
The Value are : """+str(num))
    
    # Gift
    while num == 6 :

        gift = random.randint(1,6)
        print("""OH YES!!!
Your gift is : """+str(gift))
        num = gift

# Welcome title
print("""Hello dude!Welcome to dice rolling.
-----------------------------------
___________________________________""")

# Loop
while True :

    dice()

    #Asking user to play again
    roll_again = input("Roll the Dices Again? Please enter y or n :") 

    # Exit the program
    if roll_again == 'n' :
        print("Have a good day!")
        break

    # Play again
    elif roll_again == 'y' :
        pass

    # Exception handling (y/n)
    else :
        print("Something went wrong! You didn't enter y or n.")
        break