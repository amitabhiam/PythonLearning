s = set()
#print(type(s))

#s_from_list = set([1,2,3,4])
#print(s_from_list)
s.add(1)
s.add(2)
s1 = s.union({3,4,5})
print(s,s1)
