list1 = []
num=(int(input("Enter the range: ")))
for i in range(num):
	list1.append(int(input("Enter the numbers: ")))
list2 = []
print("List two starts")
num2=(int(input("Enter the range: ")))
for i in range(num2):
	list2.append(int(input("Enter the numbers: ")))
print(list1)
print(list2)
list3=(set(list1)&set(list2))
print ("The intersection of two lists are : ", set(list3))
