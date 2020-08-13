#Map function is used to apply a function on all the elements of specified iterable and return map object.
numbers = ["3","54","45"]
numbers = list(map(int,numbers))
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

numbers[2] = numbers[2]+1
print(numbers[2])
#
# def sq(a):
#     return a*a
#
# num = [2,3,5,6,76,4,2]
# square = list(map(sq, num))
# print(square)

# #using lambda function
# num = [2,3,5,6,76,4,2]
# square = list(map(lambda x: x*x, num))
# print(square)

# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [square, cube]
# for i in range(5):
#     val = tuple(map(lambda x:x(i), func))
#     print(val)

# # Filter function create list on which given function return True.
#
# lis1 = [1,2,5,7,5,8,9,4,3]
#
# def is_greater(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater, lis1))
# print(gr_than_5)

#....REDUCE.....

from functools import reduce
##Simple way
# num = 0
# list1 = [1,2,3,4]
# for i in list1:
#     num = num+i
# print(num)

#pythonic way
from functools import reduce
list1 = [1,2,3,4]
num = reduce(lambda x,y:x+y,list1)
print(num)