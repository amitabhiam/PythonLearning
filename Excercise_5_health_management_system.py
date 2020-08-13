# Health Management System
# 3 clients - Harry, Rohan and shubham
# total 6 files- 3 for food,  3 for excercise
# write a function that when executed takes as input client name

# function to lock or retrive

# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
#
# print("which operation you want to perform\n")
# print("11 for Lock\n"
#       "21 for Retrieve\n")
# a = int(input('Enter 11 or 21\n'))
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
# if a==11:
#
#     print("1 for Harry\n"
#           "2 for Rohan\n"
#           "3 for Shubham")
#     l = int(input("Enter a  number to lock a client\n"))
#
#     if l==1:
#         f1 = open("Harry_data_ex.txt","w")
#         f1.write("Saturday: Leg day\n"
#                  "Sunday: Break\n"
#                  "Monday: Chest\n"
#                  "Tuesday: Biceps\n"
#                  "Wednesday: Shoulder\n"
#                  "Thursday: Triceps\n"
#                  "Friday: Mix")
#         f1.close()
#
#     elif l==2:
#         f2 = open("Rohan_data_ex.txt","w")
#         f2.write("Saturday: Break\n"
#                  "Sunday: Mix\n"
#                  "Monday: Chest\n"
#                  "Tuesday: Biceps\n"
#                  "Wednesday: Shoulder\n"
#                  "Thursday: Triceps\n"
#                  "Friday: Mix")
#         f2.close()
#
#     elif l==3:
#         f3 = open("Shubham_data_ex.txt","w")
#         f3.write("Saturday: Leg day\n"
#                  "Sunday: Break\n"
#                  "Monday: Biceps\n"
#                  "Tuesday: Chest\n"
#                  "Wednesday: Shoulder\n"
#                  "Thursday: Triceps\n"
#                  "Friday: Mix")
#         f3.close()
#
# if a==21:
#
#     print("1 for Harry\n"
#           "2 for Rohan\n"
#           "3 for Shubham")
#     r = int(input("Enter a  number to lock a client\n"))
#
#     if r==1:
#         f1 = open("Harry_data_ex.txt","r")
#         f11 = f1.read()
#         print(f11)
#         print(getdate())
#
#     elif r==2:
#         f2 = open("Rohan_data_ex.txt","r")
#         f22 = f2.read()
#         print(f22)
#         print(getdate())
#
#     elif r==3:
#         f3 = open("Shubham_data_ex.txt","r")
#         f33 = f3.read()
#         print(f33)
#         print(getdate())


def getdate():
    import datetime
    return datetime.datetime.now()


print("which operation you want to perform\n")
print("Enter: \n"
      "Log to enter data\n"
      "Ret to Retrieve data\n")
a = input()


def getdate():
    import datetime
    return datetime.datetime.now()

if a== "Log":

    l = input("Enter client name to lock\n")

    if l=="Harry":
        value = input("Type here\n")
        f1 = open("Harry_data_ex.txt","a")
        f1.write(str([str(getdate())]) + ": " + value + " \n")
        print('written successfully')
        f1.close()

    elif l=="Rohan":
        value = input("Type here\n")
        f2 = open("Rohan_data_ex.txt","a")
        f2.write(str([str(getdate())]) + ": " + value + " \n")
        print('written successfully')
        f2.close()

    elif l=="Shubham":
        value = input("Type here\n")
        f3 = open("Shubham_data_ex.txt","a")
        f3.write(str([str(getdate())]) + ": " + value + " \n")
        print('written successfully')
        f3.close()

    else:
        print("Invalid user name")

if a=="Ret":

    r = input("Enter client name to retreive data\n")

    if r=="Harry":
        f1 = open("Harry_data_ex.txt")
        f11 = f1.read()
        print(f11)
        # for i in f1:
        #     print(i,end=" ")

    elif r=="Rohan":
        f2 = open("Rohan_data_ex.txt")
        f22 = f2.read()
        print(f22)

    elif r=="Shubham":
        f3 = open("Shubham_data_ex.txt")
        f33 = f3.read()
        print(f33)

    else:
        print("Invalid User name")
