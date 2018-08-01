import random
print("Dictionaries")
#n=int(input("Enter the Range"))
Dict_1={}
for i in range (0,random.randint(1,15)):
	Dict_1[i] = i*i
print(Dict_1)
del Dict_1[2]
print(Dict_1)