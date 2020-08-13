#Dictionary is nothing but key value pairs
d1 = { }
#print(type(d1))
d2 = {'Harry':'Burger','Amitabh':'Prantha'}
#print(d2['Harry'])
d2['Shubham']='Alcohol'
print(d2)
#del d2['Harry']
#print(d2)

#d3 = d2
#del d3['Harry']
# print(d2)

#in above case it does not make a new dictionary d3 so to make a new copy user must use '.copy' function

d3 = d2.copy()
del d3['Harry']
print(d2)

print(d2.items())
