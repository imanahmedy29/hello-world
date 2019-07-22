name= input('Enter employee name: ')
hours_worked= float(input('Enter the number of hours worked: '))
pay_rate= float(input('Enter the hourly pay rate: '))
if hours_worked <= 40:
	weekly_salary=hours_worked*pay_rate
	print('The weekly salary earned for',name,'is', (weekly_salary))
else:
	overtime_hrs= hours_worked-40
	overtime_pr= (1.5*pay_rate)
	overtime_salary= overtime_hrs*overtime_pr
	weekly_salary=hours_worked*pay_rate
	gross_pay= weekly_salary + overtime_salary
	print('The weekly salary earned for', name, 'is', (gross_pay))