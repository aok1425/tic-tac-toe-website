# I am 1. Computer is 0. on the board
# side == 0 is when I am going. side == 1 is when computer is going.
# opp from prev alg. it's bc this side came from level. can chg back to be like prev alg
# check_win() is [score-value, move]
# in visit(), you don't know all your children until after you loop through them

from original.game import check_win, print_board, print_win
from numpy import argmin, argmax

r = {}

def init(key):
	r[key] = {
		'children': set(),
		'alpha': -10,
		'beta': 10,
		'value': None,
		'parent': None}

def test1():
	r = {}
	init('b')
	init('e')
	init('f')
	init('k')
	init('l')

	r['e']['value'] = 2
	r['k']['value'] = 3
	r['l']['value'] = 0

	r['b']['children'] = list('ef')
	r['f']['children'] = list('kl')

	visit('b', 1)
	assert r['b']['beta'] == 2
	assert r['f']['alpha'] == 3

	print 'tests pass!'

def convert_to_key(board):
	"""Takes in a board, and converts it to int to use a key in the dict r."""
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

def visit(key, side=1):
	"""key is in the str code format"""
	print 'visiting {} at side {}'.format(key, side)

	if key not in r:
		init(key)
	else:
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
			temp_pop = avail_moves.pop()
			board_copy = board[:]
			board_copy[temp_pop] = abs(side - 1) # was i before

			child_key = convert_to_key(board_copy)	

			if child_key not in r:
				init(child_key)			

			r[child_key]['parent'] = key
			r[key]['children'].add(child_key)
			visit(child_key, abs(side - 1))

			if side == 0: # even, max, alpha
				if r[child_key]['beta'] > r[key]['alpha']:
					r[key]['alpha'] = r[child_key]['beta']	
			else: # odd, min, beta
				if r[child_key]['alpha'] < r[key]['beta']:
					r[key]['beta'] = r[child_key]['alpha']					

			if r[key]['parent']:
				if side == 0:
					if r[r[key]['parent']]['beta'] < r[key]['alpha']:
						print 'going back to {} {}/{}/{}'.format(key, r[key]['alpha'], r[key]['beta'], r[key]['value'])					
						break
				else:
					if r[r[key]['parent']]['alpha'] > r[key]['beta']:
						print 'going back to {} {}/{}/{}'.format(key, r[key]['alpha'], r[key]['beta'], r[key]['value'])					
						break					

			print 'going back to {} {}/{}/{}'.format(key, r[key]['alpha'], r[key]['beta'], r[key]['value'])	

	if r[key]['parent'] == None:
		return 'children for parent are {}'.format(r[key]['children'])
		# return key # as the only key or board state w/o a parent. aka, the original one

def state_move(now, recommended):
	"""look at the diff btwn 2 strings, the current, and the recommended move, and find the index that's diff"""
	for i in range(9):
		if now[i] != recommended[i]:
			return i

def move_helper(board, side=1, memoization=False): # side=1 is when comp goes
	key = convert_to_key(board)

	if not memoization:
		visit(key)
	
	children = list(r[key]['children'])

	if side == 1: # we care abt beta, so we get the lowest alpha of our children; we are computer; we are 0
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

def test2():
	board = [0,1,0,None,1,None,1,None,None]
	# board = [1,None,None,None,None,None,None,None,None]
	print move_helper(board)
	print_board(board)

def test1():
	board = [0,1,0,1,1,0,1,None,None]
	print move_helper(board)
	print_board(board)

def test3():
	board = [1,0,1,1,0,None,0,None,None] # then computer goes
	print move_helper(board)
	print_board(board)	

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
	# benchmark()
	board = [None for i in range(9)]
	print 'I am 1. Computer is 0.'	
	play(board)	
	# test3()