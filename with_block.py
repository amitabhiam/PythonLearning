# f = open("amitabh2.txt","rt")
# #print(f.readlines())
# print(f.readline())
#
# f.close()

# using with block
# user does not have to close the file using with block, it handles it automatically

with open("amitabh2.txt") as f:
    print(f.read(4))



a = open("amitabh2.txt")
print(a.readlines())
a.close()