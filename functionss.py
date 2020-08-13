a = 5
b = 25
c = sum((a,b))
print(c)

# def is used to create user defined functions

def func1():
    print('hello you"re in function 1')

#print(func1())
#or
func1()

#input in function

def func1(c,d):
    print('hello you"re in function 1',c+d)

func1(5,7)


#def func2(e,f):
#    avg = (e+f)/2
#    print(avg)
#func2(12,56)

#use of return
def func2(e,f):
    """This is function which will calculate average"""
    avg = (e+f)/2
    print(avg)
    return avg
v = func2(12,56)
print(v)

print(func2.__doc__)

#Doc string is the first string use inside the function, its not a comment