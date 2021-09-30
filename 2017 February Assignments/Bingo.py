# Bingo Exercise 1

from random import randint
try_sum = 0
	
for k in range(0, 1000):
	prospathies = 0
	Bingo = False 
	players = []

	# Implemented for 100 players
	for i in range(0, 100):
		answers = []
		for j in range(0, 5): # 5 integers per player
			x = randint(1, 80)
			while x in answers:
				x = randint(1, 80)		
			answers.append(x)
		players.append(answers)

	# List of all the Bingo numbers given from the PC in every round
	Bingos = [] 
	while Bingo == False:
		Bingo_number = randint(1, 80) 
		while Bingo_number in Bingos:  
			Bingo_number = randint(1, 80)		
		Bingos.append(Bingo_number)

		# If a player finds one of the Bingo numbers , it becomes 0 in his answer's list.
		prospathies += 1
		for i in range(0, 100):
			for j in range(0 ,5):
				if Bingo_number == players[i][j]:
					players[i][j] = 0

		# Count the correct answers of every player, game ends when Bingo var becomes True.
		for i in range(0, 100):
			sum = 0
			for j in range(0, 5):
				if players[i][j] == 0:
					sum += 1
			if sum == 5:
				Bingo = True

	try_sum += prospathies
average_tries = try_sum / 1000.0 

print("The average tries needed for a player to find the Bingo numbers are: {}".format(average_tries))