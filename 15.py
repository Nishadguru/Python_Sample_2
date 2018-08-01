n=int(input("Enter the range"))
Dict_1={}
sum=0
for i in range (n):
	key=input("Enter the Keys")
	value=input("Enter the values")
	Dict_1.update({key:value})
	#Dict_1[key]=value
	sum = sum + int(Dict_1.get(key))
#print(Dict_1)
print("The sum of values are: ", sum)