numb=int(input("Enter the last number in the range: "))

def primed(numb):
	numb2=numb+1
	prim= range(2,numb2) #numbers with primeness to be determined 
	print('1 is not a prime number')
	print('2 is a prime number')
	for each in prim:
		for div in range(2, each): #numbers that will be divisors not including 1 or itself
			if (each%div)!=0 and (each!=div): #if it can be divided by itself (THIS HAD TO BE FIRST IDK Y)
				print(each, "is a prime number")
				break
			elif (each%div)==0: #if it can be divided by a number that is not itself
				print (each, "is not a prime number")
				break
			elif (each%div)!=0: #if it cant be divided by a number
				continue
			
primed(numb)
