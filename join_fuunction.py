#putting and in middile of items in the list - normal approch
list1 = ["John","Randy","Orton","khali","Undertaker"]

for item in list1:
    print(item, "and", end=" ")

print("other wwe superstar")

# using join function
a = " and ".join(list1)
print(a, "other wwe superstar")