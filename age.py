#Driver lisence
driving = input ('請問你有沒有開過車?')
if driving != '有' and driving !='沒有':
	print('只能輸入 有/沒有字眼')
	raise SystemExit

age = input ('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print ('你有資格考駕照')
	else:
		print('那你無照駕駛')
elif driving =='沒有':
	if age >= 18:
		print('那你可以去考駕照了')
	else:
		print('那你還要再等等')		
