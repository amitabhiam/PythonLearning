# #Pattern Printing
# input = integer n
# boolean = true/false

# True
# *
# **
# ***
# ****

# False
# ****
# ***
# **
# *

# for i in range(5):
#     for j in range(i+1):
#         if i<=5 or j<=i:
#             i = 1
#             j = 1
#             i = ++i
#         #print("*")
#             j = --j
#             print("*",end=" ")
#     print()

s = int(input('Enter 0 or 1 into program\n'))

while(s == 1):
    n = int(input('enter the no. of rows\n'))
    for i in range(n):
        for j in range(i+1):
            print('*',end=" ")
        print()
    break

while(s == 0):
    n = int(input('enter the no. of rows\n'))
    for i in range(n):
        for j in range(n-i):
            print('*',end=" ")
        print()
    break