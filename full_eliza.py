#Use random functino
#use startswith function for strings after replaced words is done
#Create 2 dictionaries (hedges and qualifiers) to add a random word to the list after replaced words

shedges = ['Please tell me more', 'Many of my patients tell me the same thing', 'It is getting late, maybe we had better quit']
squalifier = ['Why do you say that', 'You seem to think that', 'So, you are concerned that']

#Ask for user input
print('Good day. What is your problem?')
feelstring = str(input('Enter your response here or Q to quit: '))
feelstring.lower()

import random

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

	hedge = random.choice(shedges)
	qualifier = random.choice(squalifier)
	
	if feellist[0] == 'you' or feellist[0] == 'your':
		feellist.insert(0, qualifier)
		feelstring = ' '.join(feellist)
		print(feelstring)
	
	else:
		print(hedge)
	
	feelstring = str(input('Enter your response here or Q to quit: '))
	feelstring.lower()
	