import random

def newgame(): 
	def comp():
		print(f'Computer: {computer}')
	def play():
		print(f"Player: {player}")
	def won():
		print("You have won!!")
	def lost():
		print("You have lost!!") 
	def tie():
		print("Its a tie!")
	choices = ['rock','paper','scissors'] 
	computer = random.choice(choices) 
	player = None 
	while player not in choices: 
		player = input('Enter: [rock, paper or scissors]:\n') 
		player = player.lower()
	if player == computer:
		comp()
		play()
		tie()
	elif player == 'rock':
		if computer == 'scissors':
			comp()
			play()
			won()
		if computer == 'paper':
			comp()
			play()
			lost()
	elif player == 'paper':
		if computer == 'rock':
			comp()
			play()
			won()
		if computer == 'scissors':
			comp()
			play()
			lost()
	elif player == 'scissors':
		if computer == 'paper':
			comp()
			play()
			won()
		if computer == 'rock':
			comp()
			play()
			lost()
def again():
	response = input('Play again? [yes/no]\n')
	response = response.lower()
	if response == 'yes':
		return True
	else:
		return False
newgame()
while again():
	newgame()
