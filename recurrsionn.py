# def print2(str1):
#     print2(str1)  #Recurrsion condition - calling function inside the function
#     print("This is " + str1)
#
# print2("Amitabh")

# Factorial using iterative method
# def factorial(n):
#     """
#     :param n: Integer
#     :return: n * n-1 * n-2 * n-3......1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#
#     return fac
#
# number = int(input("enter the no.\n"))
# print("Factorial using iterative method",factorial(number))
## n! =  * n-1 * n-2 * n-3......1
## n! = n * (n-1)!

# Factorial using recurssive method
# def factorial_rec(n):
#     """
#     :param n: Integer
#     :return: n * n-1 * n-2 * n-3......1
#     """
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_rec(n-1)
# number = int(input("enter the no.\n"))
# print("Factorial is recurssive method",factorial_rec(number))


# n = int(input('enter the no.\n'))
# def a(num):
#     if num == 1:
#         return 1
#     else:
#         return num * a(num-1)
# print("factorial is :",a(n))


# Fibonacci series - 0 1 1 2 3 5 8 13
num = int(input("Enter the no.\n"))
print("Fibonacci series is :")
def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c

            print(c)

# fib(10)
fib(num)