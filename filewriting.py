# f = open("amitabh2.txt","w")
# # f.write("I'am writing this for you\n")
# # f.close()

# to add more content again and again open in append mode
# f = open("amitabh2.txt","a")
# f.write("I'am writing this for you\n")
# f.close()

# To check no. of characters user have written
# a = f.write("I'am writing this for you\n")
# print(a)
# f.close()

# Handle read and write both
# f = open("amitabh2.txt","r+")
# print(f.read())
# f.write("thank you")

f = open("sample_file.txt","a")
f.write(input('Write into the file\n'))
print('Sucessfully written')
f.close()

r = open("sample_file.txt","r")
content = r.read()
print(content)
r.close()
