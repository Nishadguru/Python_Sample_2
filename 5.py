list1=[]
list2=[]
#list3=[]
n1=int(input("Enter the range"))
for i in range(n1):
    list1.append(input("Enter the values"))
print("Second List Starts")
n2=int(input("Enter the range"))
for i in range(n2):
    list2.append(input("Enter the values"))

list3 = list1 + list2
print(list3)                
