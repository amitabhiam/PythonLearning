# Lambda functions or anoymous function
def add(a, b):
    print(a+b)
add(5,6)

# lambda is just one liner function
minus = lambda x,y: x-y
print(minus(9,4))

def a_first(a):
    return a[1]

a = [[1,14],[5,6]]
a.sort(key=a_first)
print(a)