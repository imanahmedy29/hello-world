
toahundred= range(1,101)
for each in toahundred:
	if each%3==0 and each%5==0:
		print("FizzBuzz")
	elif (each%3)==0:
		print("Fizz")
	elif (each%5)==0:
		print("Buzz")
	else:
		print(each)
		