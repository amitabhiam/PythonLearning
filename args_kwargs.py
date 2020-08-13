def function_name_print(a,b,c,d):
    print(a,b,c,d)
# user can give only 4 arguments while priting if more than 4 given there'll be an error
function_name_print("Harry","Rohan","Subham","Akhil")
#function_name_print("Harry","Rohan","Subham","Akhil","Amit")

# args function is used to add further arguments  in the function

def funargs(*args):
    #print(args[0]) #it'll print in indexing order
    # to print every element and more to be added
    for item in args:
        print(item)

har = ["Harry","Rohan","Subham","Akhil","Amit"]
funargs(*har)


# we can also add normal argument with *args
def funargs(normal,*args):
    print(normal)
    for item in args:
        print(item)

n = "I am normal Argument and these are students:"
har = ["Harry","Rohan","Subham","Akhil","Amit"]
funargs(n,*har)

# dealing with **kwargs
def funargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

n = "I am normal Argument and these are students:"
har = ["Harry","Rohan","Subham","Akhil","Amit"]
data = {"Amitabh":"Mastermind","Harry":"Styles","Niall":"Funny"}
funargs(n,*har,**data)

#why to use ? args when normal fucntion can do the same?
def funa(a):
    #print(args[0]) #it'll print in indexing order
    # to print every element and more to be added
    for item in a:
        print(item)

har = ["Harry","Rohan","Subham","Akhil","Amit","Ajja","kokoko","kokoka"]
funa(har)
