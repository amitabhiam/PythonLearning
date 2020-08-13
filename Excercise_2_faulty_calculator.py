#design a calculator which will correctly solve the problems except following one:
# 45*3 = 555, 56+9 = 77, 56/6 = 4
#your program should take operator and the two no. as input from the user and then return the result

a = int(input('enter first number\n'))
b = int(input('enter second number\n'))

print('select the operation you wanna perform')
sum = '+'
mul = '*'
div = '/'
sub = '-'
print(sum,mul,div,sub)
op = input('operator\n')


if a == 45 or b == 3 or op == mul:
    print(555)
elif a == 66 or b == 9 or op == sum:
    print(77)
elif a==56 or b==6 or op==div:
    print(4)
elif op == mul:
    print(a * b)
elif op == sum:
    print(a + b)
elif op == div:
    print(a/b)
elif op == sub:
    print(a-b)


#elif op==sub:
#    print(a-b)
