n1= int(input("Enter the range"))
tuple_1=[]
tuple_2=[]
for i in range (n1):
	tuple_1.append(int(input("Enter the numbers")))
print(tuple_1)
for i in tuple_1:
	tuple_2.append((i,i*i))
print(tuple_2)

"""#ALTERNATE METHORD
tuple_1=[]
for i in range (1,5):
	tuple_1.append((i,i*i))
print(tuple_1)"""
