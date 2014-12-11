# I am 1. Computer is 0. on the board
# side == 0 is when I am going. side == 1 is when computer is going.
# opp from prev alg. it's bc this side came from level. can chg back to be like prev alg
# check_win() is [score-value, move]
# in visit(), you don't know all your children until after you loop through them

from original.game import check_win, print_board, print_win
from numpy import argmin, argmax
import pickle

try:
	with open('python/board_states.pkl', "rb") as pfile:
	    r = pickle.load(pfile)
except:
	try:
		with open('board_states.pkl', "rb") as pfile:
		    r = pickle.load(pfile)
	except:
		r = {}

def init(key):
	"""Takes board state as key, and initializes values in the dictionary r."""
	r[key] = {
		'children': set(),
		'alpha': -10,
		'beta': 10,
		'value': None,
		'parent': None}

def convert_to_key(board):
	"""Takes in a board, and converts it to a key."""
	new_board = []

	for sq in board:
		if sq == None:
			new_board.append('-')
		else:
			new_board.append(str(sq))

	return ''.join(new_board)

def convert_to_board(key):
	"""Takes in a key, and converts it to board."""
	new_board = []

	for char in key:
		if char == '-':
			new_board.append(None)
		else:
			new_board.append(int(char))

	return new_board

def push_to_parent(key, child_key, side):
	"""If alpha/beta of child is better than parent's beta/alpha, depending on whether level in min or max (aka, the side), push values up."""
	if side == 0: # even, max, alpha
		if r[child_key]['beta'] > r[key]['alpha']:
			r[key]['alpha'] = r[child_key]['beta']	
	else: # odd, min, beta
		if r[child_key]['alpha'] < r[key]['beta']:
			r[key]['beta'] = r[child_key]['alpha']	

def alpha_beta_break(key, side):
	"""If node's alpha is more than parent's beta, or node's beta is less than parent's alpha, it's not worth looking deeper into tree. Return True, which will break the for loop search."""
	if r[key]['parent']:
		if side == 0:
			if r[r[key]['parent']]['beta'] < r[key]['alpha']:
				print 'going back to {} {}/{}/{}'.format(key, r[key]['alpha'], r[key]['beta'], r[key]['value'])					
				return True
		else:
			if r[r[key]['parent']]['alpha'] > r[key]['beta']:
				print 'going back to {} {}/{}/{}'.format(key, r[key]['alpha'], r[key]['beta'], r[key]['value'])					
				return True	

def visit(key, level=1): # level=1 is when computer goes
	"""Takes a key, and creates and visits all possible subsequent board states recursively in the dict r."""
	print 'visiting {} at level {}'.format(key, level)

	if key not in r:
		init(key)
	else: # memoization technique #1
		if r[key]['alpha'] != -10 and r[key]['beta'] != 10:
			return 'skipping this, already in dict'

	result = check_win(convert_to_board(key))
	board = convert_to_board(key)
	avail_moves = [i for i in range(len(board)) if board[i] == None]

	if result[0]: # no children; end of game
		print 'result is', result[1] 
		r[key]['value'] = result[1]
		r[key]['alpha'] = r[key]['value']
		r[key]['beta'] = r[key]['value']
	else:
		for i in range(len(avail_moves)): # bc i found that i can't pop() sth if it's being held by for loop
			board_copy = board[:]
			board_copy[avail_moves.pop()] = abs(level - 1) # if I make level, need to make this x % 2

			child_key = convert_to_key(board_copy)	

			if child_key not in r:
				init(child_key)			

			r[child_key]['parent'] = key
			r[key]['children'].add(child_key)
			visit(child_key, abs(level - 1))

			push_to_parent(key, child_key, level)

			if alpha_beta_break(key, level):
				break				

			print 'going back to {} {}/{}/{}'.format(key, r[key]['alpha'], r[key]['beta'], r[key]['value'])	

def state_move(now, recommended):
	"""Takes 2 different strings, and finds the index where they differ. This is the move made between the two states."""
	for i in range(9):
		if now[i] != recommended[i]:
			return i

def move_helper(board, level=1, memoization=False): # level=1 is when comp goes
	"""Takes board and creates game tree using visit().
	Returns the best move for the inputted board state, given the level/side, and child values.
	First element of output is game_state according to check_win(). Second is move."""
	key = convert_to_key(board)
	
	if not memoization: # memoization technique #2
		visit(key, level)
	
	children = list(r[key]['children'])

	if level == 1: # we care abt beta, so we get the lowest alpha of our children; we are computer; we are 0
		alphas = [r[child_key]['alpha'] for child_key in children]
		index = argmin(alphas)
		best = children[index] # key of the child that has the lowest alpha
		game_state = alphas[index] # value of the lowest alpha
	else:
		betas = [r[child_key]['beta'] for child_key in children]
		index = argmax(betas)
		best = children[index] # key of the child that has the highest beta
		game_state = betas[index] # value of the highest beta	

	return game_state, state_move(key, best)

def create_all_board_states():
	"""Cycles through all possible board states--assuming Player makes the first move--using alpha-beta pruning."""
	for i in range(9):
		board = [None for j in range(9)]
		board[i] = 1

		move_helper(board)

def pickle_board_states(obj, path):
    with open(path, "wb") as pfile:
        pickle.dump(obj, pfile)

def test1():
	board = [0,1,0,1,1,0,1,None,None]
	print move_helper(board)
	print_board(board)

def test2():
	board = [0,1,0,None,1,None,1,None,None]
	# board = [1,None,None,None,None,None,None,None,None]
	print move_helper(board, memoization=False)
	print_board(board)

def test3():
	board = [1,0,1,1,0,None,0,None,None] # then computer goes
	print move_helper(board)
	print_board(board)	

def test4():
	board = [1,0,1,1,0,None,0,None,None] # then computer goes
	visit(convert_to_key(board))

def play(board):
	while None in board:
		print_board(range(9))
		print ''
		print_board(board)

		board[int(raw_input('Which space? '))] = 1 # I go first always, instead of computer
		print_board(board)

		if check_win(board)[0]:
			print_win(board)
			break

		print '\nNow, computer goes...\n'

		move = move_helper(board, memoization=True)
		print move
		board[move[1]] = 0
		print_board(board)
		print '\n'

		if check_win(board)[0]:
			print_win(board)
			break

def benchmark():
	board = [None for i in range(9)]
	board[1] = 1
	print move_helper(board, memoization=False)

if __name__=='__main__':
	benchmark()
	# board = [None for i in range(9)]
	# print 'I am 1. Computer is 0.'	
	# play(board)	
	# test1()