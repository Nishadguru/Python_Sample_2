#1. Python Program to Find the Largest Number in a List

list1 =[]
num = int(input("Range"))
for i in range(num):
	list1.append(int(input("Enter")))
list1.sort()
print(list1[-2]) 
