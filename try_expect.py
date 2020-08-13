# try except is used when user wants to ignore a execution in middle of program if it's wrong and doesn't affect
# the rest of the program...which can be important.
print('enter num1')
num1 = input()
print('enter num2')
num2 = input()
try:
    print('the sum of two numbers is :',int(num1)+int(num2))
except Exception as e:
    print(e)

print('this line is important')