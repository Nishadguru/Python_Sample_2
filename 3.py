list1 = []
num =int(input("Enter the range"))
for i in range (num):
	list1.append(int(input("Enter the values")))
odd_list=[]
even_list=[]

for i in range (0,len(list1)):
	if list1[i]%2 == 1:
		odd_list.append(list1[i])
	else:
		even_list.append(list1[i])

print("The odd numbers are  : ",odd_list)
print("The even numbers are : ",even_list)
