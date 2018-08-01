n=int(input("Enter the range"))
Dict_1={}
mul=1
for i in range (n):
	key=input("Enter the Keys")
	value=input("Enter the values")
	Dict_1.update({key:value})
	#Dict_1[key]=value
	mul = mul * int(Dict_1.get(key))
print(Dict_1)
print("Product of the values are: ", mul)