import random

responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

quest = str(input('\nYOU ASKED: '))

def magic8():
	response = random.choice(responses)
	print('\nMAGIC 8-BALL SAYS:', response)
	
	
magic8()
cont = str(input('\nDo you have another question for the Magic 8-Ball? (y/n):  '))
cont = cont.lower()

while cont != 'n':
	quest = str(input('\nYOU ASKED: '))
	magic8()
	cont = str(input('\nDo you have another question for the Magic 8-Ball? (y/n):  '))
	cont = cont.lower()
else:
	print('\nThank you for playing!\n')
