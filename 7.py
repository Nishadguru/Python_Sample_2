list1=[]
list2=[]
list3=[]
n1=int(input("Enter the range"))
for i in range(n1):
    list1.append(input("Enter the values"))
  
print("Second List Starts")

n2=int(input("Enter the range"))
for i in range(n2):
    list2.append(input("Enter the values"))
print(list1)
print(list2)
list3 =(set(list1)|set(list2))
print("The union of numbers are: ",set(list3))
list4=(set(list1)&set(list2))

print ("The intersection of two lists are : ", set(list4))








"""list1 = []
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
print ("The intersection of two lists are : ", set(list3))"""

