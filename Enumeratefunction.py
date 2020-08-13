list1 = ["Bhindi","Aloo","Chopsticks","chowmein"]

#noraml approch
# i = 1
# for item in list1:
#     if i%2 is not 0:
#         print(f"Jarvis Please buy {item}")
#     i += 1

#using enumerate function

for index,item in enumerate(list1):
    if index%2 == 0:
        print(f"Jarvis Please buy {item}")