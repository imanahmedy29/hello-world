print('Good day. What is your problem?')

#Ask for user input
feelstring = str(input('Enter your response here or Q to quit: '))
feelstring = feelstring.lower()

#Replacement word information
#replacements = {'i':'you', 'me':'you', 'my':'your', 'am':'are'}
#initials = ['i', 'me', 'my', 'am']
#finals = ['you', 'you', 'your', 'are']

#Need a running loop
while feelstring != 'q':	
	#feelstring is a string
	
	feellist = feelstring.split()
	#feellist is a list

	for key, value in {'i':'you', 'me':'you', 'my':'your', 'am':'are'}.items():
		for item in feellist:
			if item == key:
				indx = feellist.index(key)
				feellist[indx] = value

	feellist.insert(0, 'why do you say that')
	
	feelstring = ' '.join(feellist)
	print(feelstring)
	
	feelstring = str(input('Enter your response here or Q to quit: '))
	feelstring = feelstring.lower()
	
#THIS DIDNT WORK
#TRY1
	#for key in replacements:
		#feel.replace(key, replacements[key])

#TRY2		
	#for initial, final in replacements.items():
	#	indx = feel.find(initial)
	#	print(indx) #check1
	#	feels[indx] = final

#TRY3
	#for me in initials:
	#	for word in feels:
	#		if me == word:
	#			indx = initials.index(me)
	#			feels[indx] = finals[indx]
	#			print(indx) #check1
				
#TRY4: THIS WORKS BUT	
	#the problem with this is that the inputted feelstring cannot have i, my, am me ending a word
	#for key, value in {'i ':'you ', 'me ':'you ', 'my ':'your ', 'am ':'are '}.items():
		#feelstring = feelstring.replace(key, value)

	
	