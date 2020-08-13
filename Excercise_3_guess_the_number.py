#n = 18
# no. of guesses 9
# print no. of guesses left
# no. of guesses he took to finish
# game over
c = 1
a = 18
while(c<=9):
    b = int(input('enter the number\n'))
    if b>a:
        print('number is greater\n')
    elif b<a:
        print('number is lesser\n')
    else:
        print('guess is right\n')
        print(c,'guesses user took to finish.')
        break
    print(9-c,'no. of guesses left\n')
    c = c+1
if(c>9):
    print('game over')