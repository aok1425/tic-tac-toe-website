# I am 1. Computer is 0. on the board and in move_helper()
# check_win() is [score-value, move]

# 12/11/14: added choose_first. If True, once program finds a winning set of routes, it will stop searching and do that set.
# Thinking behind this is that it would choose the quickest way to win.
# But actually, it will choose the first one it sees, in the tree going from left to right.
# So it may not choose the quickest way, but rather the way that involves the first empty space it sees, reading top-down, left-right.

# Does this also function as alpha-beta pruning? It stops the for loop. So maybe it's both choose_first and alpha-beta?

# It's like quasi-alpha-beta. I think it only works bc leaf node values are 1/-1/0. So, we can stop the for loop if we get to a max value.
# That's not how alpha-beta works. That works by comparing the value (alpha/beta) to the value of its parent node.
# This quasi-alpha-beta doesn't look at the parent node. It just stops the for loop if it finds a desired max value at the leaf node.

# I still don't understand how the alg finds the best path if, say, it has multiple paths to a win.
# My understanding is that it just chooses the most recent path, going left to right
# Maybe after I make the first move, all the paths get back as a tie, so it doesn't run into the above problem.
# Any way to print things to find out?

from check_win_recursively import check_win

def print_board(board):
	print ' '.join(['-' if i == None else str(i) for i in board][:3])
	print ' '.join(['-' if i == None else str(i) for i in board][3:6])
	print ' '.join(['-' if i == None else str(i) for i in board][6:])

def play(board, choose_first=False):
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

		move = move_helper(board, 0, choose_first)
		print move
		board[move[1]] = 0
		print_board(board)
		print '\n'

		if check_win(board)[0]:
			print_win(board)
			break

def play_computer_first(board):
	while None in board:
		print '\nComputer goes...\n'

		move = move_helper(board, 0)
		#print move
		board[move[1]] = 0
		print_board(board)
		print '\n'

		if check_win(board)[0]:
			print_win(board)
			break

		print_board(range(9))
		print ''
		print_board(board)

		board[int(raw_input('Which space? '))] = 1 # I go first always, instead of computer
		print_board(board)

		if check_win(board)[0]:
			print_win(board)
			break

def print_win(board):
	result = check_win(board)[1]
	if result == 1:
		print 'Player wins'
	elif result == 0:
		print 'Tie'
	elif result == -1:
		print 'Computer wins'

def move_helper(board, side=0, choose_first=True):
	"""Side=0 is when computer goes. If choose_first=True, computer will pick the first winning path instead of continuing to find other possible winning paths.
	This works in tic-tac-toe bc you can only win/lose/tie, 1/-1/0. If there were other end game states, choose_first wouldn't work."""
	board = board[:] # copies the list board
	best = [None, None] # score-value, move

	result = check_win(board)
	if result[0]:
		return [result[1]]

	if side == 0:
		best[0] = 1
	else:
		best[0] = -1

	avail_moves = [i for i in range(len(board)) if board[i] == None]

	for i in range(len(avail_moves)):
		temp_pop = avail_moves.pop()
		board_copy = board[:]
		board_copy[temp_pop] = side
		reply = move_helper(board_copy, abs(side - 1))

		if (side == 0 and reply[0] <= best[0]) or (side == 1 and reply[0] >= best[0]):
			best[0] = reply[0]
			best[1] = temp_pop

		if choose_first:
			if (side == 0 and reply[0] == -1) or (side == 1 and reply[0] == 1):
				return best	

	return best

def test1():
	board = [0,1,0,None,1,None,1,None,None]
	print_board(board)

	print move_helper(board, 0)

def test2():
	board = [1,0,0,0,1,1,None,1,None] # then computer goes
	print_board(board)
	print move_helper(board, 1)
	# play_computer_first(board)

def test3():
	board = [1,0,1,None,0,None,1,None,None] # then computer goes
	print_board(board)
	print move_helper(board, 0)
	# play(board) # don't choose 2

def test4(i):
	board = [None for i in range(9)]
	board[i] = 1
	print move_helper(board, 0)

def test5(sq, board):
	board = board[:]
	board[sq] = 1
	print 'checking slow version on', sq
	slow = move_helper(board, 0)
	print slow
	print 'checking fast version'
	fast = move_helper(board, 0, True)
	print fast
	assert fast == slow
	print 'both fast and slow like', fast

def test6():
	board = [None for i in range(9)]
	# board = [1,0,None,None,None,None,0,None,None] # then computer goes	

	for i in range(2,9):
		try:
			test3(i, board)
		except:
			print 'didn\'t pass'

def test2():
	board = [0,1,0,None,1,None,1,None,None]
	# board = [1,None,None,None,None,None,None,None,None]
	print move_helper(board, 0)
	print_board(board)

def benchmark():
	board = [None for i in range(9)]
	board[1] = 1
	print move_helper(board)

if __name__=='__main__':
	# benchmark()
	# board = [None for i in range(9)]
	# play(board, False)
	test3()