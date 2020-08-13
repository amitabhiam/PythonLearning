# time module is used to find the execution time of any program
import time

initial = time.time()

k = 0
while(k<5):
    print("This is Amitabh")
    time.sleep(2)
    k+=1
print("while loop time",time.time() - initial,"Seconds")

initial2 = time.time()
for i in range(45):
    print("This is Amitabh")
print("for loop time",time.time() - initial2,"Seconds")

# To check the current time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

# To create time delay time.sleep fuction is used
#time.sleep(2)