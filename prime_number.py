num = int(input("Enter the no.\n"))

for i in range(2,10):
    if num % i == 0:
        print("Not Prime")
        break
    else:
        print("Prime")
