import random
import string
def make_cipher():
	string=str(input("Enter the Word: "))
	nstring=''
	for i in string:
		if i not in nstring:
			nstring +=i 
	print(nstring)
	shuttle_str(nstring)
		

def shuttle_str(nstring):
	dict={}
	for i in nstring:
 		dict[i]= random.choice(string.ascii_lowercase)
	print("The Dictionary is : ")
	print(dict)
	display_cipher(dict,nstring)

def display_cipher(dict,nstring):
	new_val=''
	for i in nstring:
		new_val += dict[i]
	print(new_val)

#Calling Methords
make_cipher()