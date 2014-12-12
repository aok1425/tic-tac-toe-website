# I am 1. Computer is 0. on the board and in move_helper()
# check_win() returns [score-value, move]

# 12/11/14: added choose_first. If True, once program finds a winning set of routes, it will stop searching and do that set.
# Thinking behind this is that it would choose the quickest way to win.
# But actually, it will choose the first one it sees, in the tree going from left to right.
# So it may not choose the quickest way, but rather the way that involves the first empty space it sees, reading top-down, left-right.

from check_win_recursively import check_win

def print_board(board):
	print ' '.join(['-' if i == None else str(i) for i in board][:3])
	print ' '.join(['-' if i == None else str(i) for i in board][3:6])
	print ' '.join(['-' if i == None else str(i) for i in board][6:])

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

		move = move_helper(board, 0)
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

def move_helper(board, side=0, parent=[False], memoization=None): # side=0 is computer's turn; memoization is to make this fn compatible w newer one, so app.py can call either one
	"""Side=0 is when computer goes. If choose_first=True, computer will pick the first winning path instead of continuing to find other possible winning paths.
	This works in tic-tac-toe bc you can only win/lose/tie, 1/-1/0. If there were other end game states, choose_first wouldn't work."""
	board = board[:] # copies the list board

	result = check_win(board)
	if result[0]:
		return [result[1]]

	if side == 0:
		current = [1, None] # score-value, move
	else:
		current = [-1, None]

	avail_moves = [i for i in range(len(board)) if board[i] == None]

	for i in range(len(avail_moves)):
		temp_pop = avail_moves.pop()
		board_copy = board[:]
		board_copy[temp_pop] = side
		child = move_helper(board_copy, abs(side - 1), parent=current)

		# regular Minimax
		if (side == 0 and child[0] <= current[0]) or (side == 1 and child[0] >= current[0]):
			current[0] = child[0]
			current[1] = temp_pop

		# choose-first. can only happen in tic-tac-toe, when win state = best possible outcome. ie no multiple win values
		if (side == 0 and child[0] == -1) or (side == 1 and child[0] == 1):
			# print 'choose_first'
			return current # breaks the for loop

		# alpha-beta pruning
		if (side == 0 and parent[0] > current[0]) or (side == 1 and parent[0] < current[0]):
			# print 'alpha-beta'
			return current # breaks the for loop

	return current

def test1():
	board = [0,1,0,None,1,None,1,None,None]
	print_board(board)

	print move_helper(board, 0)

def test2():
	board = [1,0,0,0,1,1,None,1,None] # then computer goes
	print_board(board)
	print move_helper(board, 0)
	# play_computer_first(board)

def test3():
	board = [1,0,1,None,0,None,1,None,None] # then computer goes
	print_board(board)
	print move_helper(board, 0)
	# play(board) # don't choose 2

def test4():
	board = [None for i in range(9)]
	board[1] = 1
	print move_helper(board)
	print_board(board)

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

def test5(): # why does this return [1,1]? i don't see how player will win here.
	board = [1, None, 1, None, None, 0, None, None, None]
	print move_helper(board)
	print_board(board)	

def benchmark():
	board = [None for i in range(9)]
	board[1] = 1
	print move_helper(board)

if __name__=='__main__':
	benchmark()
	# board = [None for i in range(9)]
	# play(board)
	# test5()