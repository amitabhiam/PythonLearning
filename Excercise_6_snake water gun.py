# Snake water Gun
# using random function
#play 10 times
#choose one among 3
#take input from user - S,W or G

import random

ucount = 0
ccount = 0
op = 1
choices = ["Stone","Paper","Scissor"]


while op<11:
    a = input("Enter your choice:\n"
              "Stone  Paper  Scissor\n")
    fun = random.choice(choices)

    if a =='Stone' and fun == 'Scissor':
        print("you won\n")
        ucount = ucount+1
    elif a =='Stone' and fun == 'Paper':
        print("Computer won\n")
        ccount = ccount+1
    elif a =='Stone' and fun == 'Stone':
        print("Tie")

    elif a =='Scissor' and fun == 'Scissor':
        print("tie")
    elif a =='Scissor' and fun == 'Paper':
        print("You won")
        ucount = ucount + 1
    elif a =='Scissor' and fun == 'Stone':
        print("Computer won")
        ccount = ccount + 1

    elif a =='Paper' and fun == 'Paper':
        print("tie")
    elif a =='Paper' and fun == 'Stone':
        print("You won")
        ucount = ucount + 1
    elif a =='Paper' and fun == 'Scissor':
        print("Computer won")
        ccount = ccount + 1
    else:
        print("Invalid Input\n")

    print("No. of chances left\n",10-op)
    op = op + 1

if(op>=10):
    print("Game Over")
if ccount>ucount:
    print("Computer won the game")
elif ccount==ucount:
    print("Game is tied")
else:
    print("you won the game")