"""print("Dictniories")
Dict_1={'Nishad':'cloud computing','Ashwath':'Big data', 'Balaje':'Embeded Systems', 'Arjun':'Internet of Things'}
Dict_2={'vinod':'Srinsoft','Nivetha':'SB International', 'Pratibha':'TCS PVT LTD', 'Prasanna':'SHELL Distributor'}
print(Dict_1)
print(Dict_2)
Dict_1.update(Dict_2)
print(Dict_1)"""



#USING METHORDS

print("Dictniories")

def Dicts_1():
	Dict_1={'Nishad':'cloud computing','Ashwath':'Big data', 'Balaje':'Embeded Systems', 'Arjun':'Internet of Things'}
	Dict_2={'vinod':'Srinsoft','Nivetha':'SB International', 'Pratibha':'TCS PVT LTD', 'Prasanna':'SHELL Distributor'}
	print(Dict_1)
	print(Dict_2)
	Dict_1.update(Dict_2)				
	print(Dict_1)
	return Dict_1, Dict_2

Dicts_1()