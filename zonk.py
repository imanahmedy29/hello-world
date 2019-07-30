
dir = str(input('\nEnter the direction you would like to go (e/w/n/s) or q to quit: \t'))
dir = dir.lower()
visited_rooms = 0
coordinates_x = 0
coordinates_y = 0
coordinates = [coordinates_x, coordinates_y]

chance_25 = ['y', 'n', 'n', 'n']
import random 

def dire():
	dir = str(input('\nEnter the direction you would like to go (e/w/n/s) or q to quit: \t'))
	dir = dir.lower()
	
	#decide coordinates for each room
	#decide start position
	#put in secret room coordinates and chances

def rooms(coordinates_x, coordinates_y):
	if dir == 'e':
		coordinates_x = coordinates_x + 1
	elif dir == 'w':
		coordinates_x = coordinates_x - 1
	elif dir == 'n':
		coordinates_y = coordinates_y + 1
	elif dir == 's':
		coordinates_y = coordinates_y - 1
	else:
		print('This is not an option, please input a direction (e/w/n/s) or q to quit.')
	coordinates = [	coordinates_x, coordinates_y]


def quitting():
	print('\nYou are leaving the house')
	haunting = random.choice(chance_25)
	if haunting == 'y':
		print('\nWatch out! You are being followed by a ghost!')
		print('\nWhile here, you visited', visited_rooms, 'rooms. Thank you for playing! Goodbye,')
	else: 
		print('\nWhile here, you visited', visited_rooms, 'rooms. Thank you for playing! Goodbye.\n')

def foyer():
	print("\nWelcome to the foyer. You are in room 1. This room contains a dead scorpion, but there's nothing to be scared of!")

def frontroom():
	print('\nWelcome to the front room. You are in room 2. This room contains a piano. Give it a play!')

def library():
	print("\nWelcome to the library. You are in room 3. This room contains spiders. But don't let that stop you from reading!")
	
def kitchen():
	print('\nWelcome to the kitchen. You are in room 4. This room contains bats, that are definitely not for eating.')
	
def diningroom():
	print('\nWelcome to the dining room. You are in room 5. This room contains dust and an empty box. I know: disappointing')

def vault():
	print('\nWelcome to the vault. You are in room 6. This room contains 3 walking skeletons. Better run!')
	
def parlor():
	print('\nWelcome to the parlor. You are in room 7. This room contains a treasure chest. Nice!')
	
def secretroom():
	print('\nWelcome to the secret room. You are in room 8. Few have made it here. This room contains piles of gold. Do with it what you wish, but be careful when leaving.')
	
#def farout():
#	if coordinates_x > 2:
#		print("\nThese are your current coordinates:", coordinates, "in the (x,y) coordinate system")
#		print('You moved too far out east. Try coming back to the center')
#	elif coordinates_x < -2:
#      	print("\nThese are your current coordinates:", coordinates, "in the (x,y) coordinate system")
#		print('You moved too far out west. Try coming back to the center')
#	elif coordinates_y < -1:
#		print("\nThese are your current coordinates:", coordinates, "in the (x,y) coordinate system")
#		print('You moved too far out south. Try coming back to the center')
#	elif coordinates_y > 4:
#       print("\nThese are your current coordinates:", coordinates, "in the (x,y) coordinate system")
#		print('You moved too far out north. Try coming back to the center')
#	else:
#		dire()
#		rooms()

while dir != 'q':
	if dir == 'e':
		coordinates_x = coordinates_x + 1
	elif dir == 'w':
		coordinates_x = coordinates_x - 1
	elif dir == 'n':
		coordinates_y = coordinates_y + 1
	elif dir == 's':
		coordinates_y = coordinates_y - 1
	else:
		print('\nThis is not an option, please input a direction only as e, w, n, or s/n')
		dir = str(input('\nEnter the direction you would like to go (e/w/n/s) or q to quit: \t'))
		dir = dir.lower()
	coordinates = [coordinates_x, coordinates_y]
	print(coordinates) #check
	if coordinates_x > 2:
		print("\nThese are your current coordinates:", coordinates, "in the (x,y) coordinate system")
		print('You moved too far out east. Try coming back to the center')
	elif coordinates_x < -2:
		print("\nThese are your current coordinates:", coordinates, "in the (x,y) coordinate system")
		print('You moved too far out west. Try coming back to the center')
	elif coordinates_y < -1:
		print("\nThese are your current coordinates:", coordinates, "in the (x,y) coordinate system")
		print('You moved too far out south. Try coming back to the center')
	elif coordinates_y > 4:
		print("\nThese are your current coordinates:", coordinates, "in the (x,y) coordinate system")
		print('You moved too far out north. Try coming back to the center')
	elif coordinates_x == 0 and coordinates_y == 1:
		foyer()
		visited_rooms += 1
	elif coordinates_x == 0 and coordinates_y == 2:
		frontroom()
		visited_rooms += 1
	elif coordinates_x == 0 and coordinates_y == 3:
		vault()
		visited_rooms += 1
	elif coordinates_x == 1 and coordinates_y == 2:
		kitchen()
		visited_rooms += 1
	elif coordinates_x == (-1) and coordinates_y == 3:
		diningroom()
		visited_rooms += 1
	elif coordinates_x == (-1) and coordinates_y == 2:
		kitchen()
		visited_rooms += 1
	elif coordinates_x == 1 and coordinates_y == 3:
		sec_rm = random.choice(chance_25)
		if sec_rm == 'y':
			secretroom()
			visited_rooms += 1
		else: 
			parlor()
			visited_rooms += 1
	print("You haven't found a room yet. Keep exploring!")
	dire()	
else: 
	quitting()	

			
	
	
	