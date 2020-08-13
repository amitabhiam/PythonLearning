
l = 9   # Global variable
def function1(n):
    #l=5  #Local variable
    # global keyword is used to read global variable in local scope
    global l
    l = l + 5
    print(l)
    print(n, "I have printed")

# function1("This is me")
# print(l)


def harry():
    x = 20

    def rohan():
        global x
        x = 88
    print("before calling rohan()",x)
    rohan()
    print("after calling rohan()",x)

harry()

# x = 10
# def main():
#     # x = 45
#     global x
#     y=x+x
#     print(y)
#     def sec():
#         global x
#         z = y+x
#         print(z)
#         sec()
#
# main()
