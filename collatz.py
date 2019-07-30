
numb=int(input("Enter a number: "))
def collatz(numb):
	print(numb)
	while numb>1:
		if numb%2==0:
			numb=numb//2
			print(numb)
		else: 	
			numb=(numb*3)+1
			print(numb)

collatz(numb)	
ques=input("Would you like to input another number? ")

while ques=="yes":
	numb=int(input("Enter a number: "))	
	collatz(numb)
	ques=input("Enter yes if you like to input another number: ")
	