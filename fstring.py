# F Strings - best way for string formatting
# types of string formatting - %s , .format(), fstring

#simple
me = "Amitabh"
a = "This is %s"%me
print(a)

# .format()
me = "Amitabh"
a1 = 21

a = "This is {} {}"
b = a.format(me,a1)
print(b)

# F string
import math
fs = f"this is {me} {a1} {4*56} {math.cos(45)}"
print(fs)