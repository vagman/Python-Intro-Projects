#Bingo Askisi 1

import random
try_sum = 0
	
for k in range(0,1000):
	prospathies = 0
	Bingo = False # Flase so that While on line 20 begins working
	players = []
	for i in range(0,100): # 100 players
		answers = []
		for j in range(0,5): # 5 integers per player
			x = random.randint(1,80)
			while x in answers:
				x = random.randint(1,80)		
			answers.append(x)
		players.append(answers)

	Bingos = [] # List of all the Bingo numbers given from the PC in every round
	while Bingo == False:
		Bingo_number = random.randint(1,80) #Brings up a random number
		while Bingo_number in Bingos:  # Genrates diffrent numbers every time
			Bingo_number = random.randint(1,80)		
		Bingos.append(Bingo_number)

#If a player finds one of the Bingo numbers , it becomes 0 in his answer's list.

		prospathies += 1
		for i in range(0,100):
			for j in range(0,5):
				if Bingo_number == players[i][j]:
					players[i][j] = 0

# This nested For loop counts the correct answers of every player.
# Game ends when Bingo var becomes True.

		for i in range(0,100):
			sum = 0
			for j in range(0,5):
				if players[i][j] == 0:
					sum += 1
			if sum == 5:
				Bingo = True

	try_sum += prospathies
average = try_sum/1000.0 
print "The average tries needed for a player to find the Bingo number are: ", average