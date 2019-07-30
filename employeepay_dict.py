Mary = {'15': '40'}
John = {'22': '25'}
Bob = {'35': '4'}
Mel = {'43': '62'}
Jen = {'17':'33'} 
Sue = {'29':'45'}
Ken = {'40':'36'}
Dave = {'20':'17'}
Beth = {'37':'37'}
Ray = {'16.5':'80'}
employees = [Mary, John, Bob, Mel, Jen, Sue, Ken, Dave, Beth, Ray] 
first_names = ['Mary', 'John', 'Bob', 'Mel', 'Jen', 'Sue', 'Ken', 'Dave', 'Beth', 'Ray']

def calculations():
	for variable in employees:
		position = employees.index(variable)
		for hours, pay in variable.items():
			hours = float(hours)
			pay = float(pay)
			if hours <= 40:
				weekly_s = hours * pay
				print('\nThe weekly salary earned for',first_names[position],'is', (weekly_s))
			else:
				overtime_hrs = hours - 40
				overtime_pr = (1.5 * pay)
				overtime_s = overtime_hrs*overtime_pr
				weekly_s = hours * pay
				gross_pay = weekly_s + overtime_s
				print('\nThe weekly salary earned for', first_names[position], 'is', (gross_pay))
			
calculations()
			
#res = str(input("Would you like to store another employee's information? If not, type q:"))
#res.lower()

#def additions(name, hrs, rate):
#	hrs = str(input('Hours worked ='))
#	rate = str(input('Pay rate = '))
#	name = str(input('Employee name:'))
#	name = {hrs : rate}
#	employees = employees.append(name)
#	first_names = first_names.append(name)
	
#	res = str(input("Would you like to add another employee's information? If not, type q:"))
#	res.lower()

#while res != 'q':
#	additions(name, hrs, rate)
 


