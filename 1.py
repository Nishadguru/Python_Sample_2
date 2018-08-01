#1. Python Program to Find the Largest Number in a List

list1 =[]
num = int(input("Range"))
for i in range(num):
	list1.append(int(input("Enter")))
list1.sort()
print(list1[-1])  


# ALTERNATE LOGIC:

"""num = (input("Enter the numbers"))
numlist = num.split(' ')
large = numlist[0]
for i in range(len(numlist)):
	if (int(large)<int(numlist[i])):
		large=numlist[i]
print(large)"""



