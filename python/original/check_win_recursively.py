# sth abt scope, the fact that in while loops, that's not global scope
# and for fns in while loops, they wld only take global scope

# explaining the crazy, crazy recursion i have going on below

# look through each square, in NumPy so that i can use my 'compass'
# if a square is 1, append that to the history list
# there is a new history list for each square
# then, look through all the directions on the compass
# if there is a 1 after moving the one square in the direction according to direction,
# save that direction
# then, look move another square in the same direction and see if there's a 1 there
# if not, remove the last move out of history
# then, the computer will look at the next direction, and see if there's a 1 there
# this way, history always starts with the first square before it cycles through all the directions
# and adds more squares onto history if they are 1

# the computer checks if there are 3 squares in history ONLY AFTER it removes a square if there are no other squares that 1 in the subseq sq
# thus, right before it removes a square after 3 sqs in hx, it now checks if there are 3 sqs in hx. if so, it doesn't pop()
# that way, after there are 3 squares, just because there isn't a 4th one, it doesn't remove that 3rd sq when the comp checks for 3 sqs to determine win condition

# next steps:

# double-check that it works for grids larger than 3x3

import numpy as np
from math import isnan

def print_board(board):
	print ' '.join(['-' if isnan(i) else str(i) for i in board][:3])
	print ' '.join(['-' if isnan(i) else str(i) for i in board][3:6])
	print ' '.join(['-' if isnan(i) else str(i) for i in board][6:])

def check_win(board, max_board_length=3):
	"""Input a board, and find out the state of the game, whether win, lose, tie, or game not over.
	Output is a list. First element is whether the game is over. Second element is the state of the game (win/lose/tie) if it is over."""
	board = board[:]

	for i in range(len(board)):
		if board[i] == None:
			board[i] = np.NaN

	# print board

	n = np.array(board).reshape(3,3)
	it = np.nditer(n, flags=['multi_index'])
	counter = 0

	def check_squares(new_position, direction, history, player):
		"""history refers to either history1s or history0s"""
		# print 'hx starts at', history
		if new_position[0] < max_board_length and new_position[1] < max_board_length and new_position[0] >= 0 and new_position[1] >= 0:
			if n[new_position] == player and new_position not in history:
				history.append(new_position)
				# print '\t', history, 'under direction', direction

				new_position = tuple([new_position[0] + direction[0], new_position[1] + direction[1]])

				if (not check_squares(new_position, direction, history, player)) and len(history) != 3:
					# print 'popping'
					history.pop()
			
				return True

	while not it.finished: 
		# print 'square', counter
		# counter += 1
		value = it[0]
		position = it.multi_index

		history1s = []
		history0s = []

		xs = [0,1,0,-1,-1,-1,1,1]
		ys = [1,0,-1,0,-1,1,1,-1]

		if value == 1:
			history1s.append(position)
			# print 'we found the 1st 1 at', position

			for i in range(len(xs)):
				direction = [xs[i], ys[i]]
				# print 'direction is', direction
				new_position = tuple([position[0] + direction[0], position[1] + direction[1]])

				check_squares(new_position, direction, history1s, 1)
				
				# print len(history)

				if len(history1s) == 3:
					# print history1s
					return [True, 1]	
		
		if value == 0:
			history0s.append(position)
			# print 'we found the 1st 1 at', position

			for i in range(len(xs)):
				direction = [xs[i], ys[i]]
				# print 'direction is', direction
				new_position = tuple([position[0] + direction[0], position[1] + direction[1]])

				check_squares(new_position, direction, history0s, 0)
				
				# print len(history)

				if len(history0s) == 3:
					# print history0s
					return [True, -1]

		it.iternext()

	if np.NaN not in board: # a tie
		return [True, 0]

	return [False] # not a tie; no one has one

def check_win(board):
	"""Simplified fn, assuming that board size will always be 3x3.
	Input board and output game state.
	First element is whether game is over. Second, optional, element is who has won game, or tie."""
	win_positions = [123, 456, 789, 147, 258, 369, 159, 357]

	for marker in [0,1]:
		for position in win_positions:
			indices = [int(i) - 1 for i in list(str(position))]

			if False not in [board[i] == marker for i in indices]:
				if marker == 0:
					return [True, -1] # Computer wins/Player loses
				else:
					return [True, 1] # Player wins/Computer loses

	if None in board:
		return [False] # game not over
	else:
		return [True, 0] # tie

def test():
	board = [1,0,0,0,1,1,None,1,0]
	assert check_win(board) == [False]

	board = [1,0,0,0,1,1,0,1,0]
	assert check_win(board) == [True, 0]

	board = [1,0,0,0,1,0,1,0,1]
	assert check_win(board) == [True, 1]

	board = [1,1,1,0,0,None,0,None,None]
	assert check_win(board) == [True, 1]

	board = [None,0,None,None,0,None,1,0,1]
	assert check_win(board) == [True, -1]

	print 'tests pass!'

if __name__=='__main__':
	test()