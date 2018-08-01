sentence=str(input("Enter a sentence: "))
sentence=sentence.split(' ')
big = 0
for i in sentence:
	if len(i)>big:
		big=len(i)
		word = i           #to display the longest word
print("The Longest word in the sentence is ", big)
print (word)