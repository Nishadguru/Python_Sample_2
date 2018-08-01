num1=int(input("Enter the Range: "))
list1=[]
for i in range(num1):
        list1.append(input("Enter the numbers: "))
num2 =int(input("Enter the number: "))
list2=[]
print("Second list starts")
for i in range(num2):
        list2.append(input("Enter the numbers: "))
if (len(list1)==len(list2)):
    print("The lists are equal")
else:
    print("The list are not equal")

""" If we need to see the values are equal

if (list1[i]==list2[i]):
    print("The lists are equal")
else:
    print("The list are not equal") """


