print('Good day. What is your problem?')

#Ask for user input
feels = str(input('Enter your response here or Q to quit: '))
feels.lower()

#Need a running loop
while feels != 'q':	
	print(feels)
	feels = str(input('Enter your response here or Q to quit: '))
	feels.lower()
	
	
	