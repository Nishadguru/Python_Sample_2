dict_marks={'nishad':{'cc':97,'dba':80,'vlsi':75, 'emb':85, 'cv':87},
'achyuth':{'cc':100,'dba':100,'vlsi':100,'emb':95, 'cv':97},
'shreyank':{'cc':98,'dba':87,'vlsi':89,'emb':95, 'cv':97}}

def student_marks(dict_marks):
	for i in dict_marks:
		for i1 in dict_marks[i]:
			if int(dict_marks[i][i1]) in range (90,101):
				dict_marks[i][i1] = 'A+'
			elif int(dict_marks[i][i1]) in range (80,89):
				dict_marks[i][i1] = 'A'
			elif int(dict_marks[i][i1]) in range (70,79):
				dict_marks[i][i1] = 'B'
			elif int(dict_marks[i][i1])  in range (60,69):
				dict_marks[i][i1] = 'C'
			elif int(dict_marks[i][i1]) in range (50,59):
				dict_marks[i][i1] = 'D'
			else:
				dict_marks[i][i1] = 'Makeup'
	print(dict_marks)
		

student_marks(dict_marks)