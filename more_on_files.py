f = open("amitabh2.txt")
# f.tell is used to know where the file pointer is:
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())

# f.seek is used to reset the file pointer

f.seek(0)
print(f.readline())

f.seek(10)
print(f.readline())

f.close()