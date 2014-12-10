# I am 1. Computer is 0. on the board and in move_helper()
# check_win() is [score-value, move]

# I still don't understand how the alg finds the best path if, say, it has multiple paths to a win.
# My understanding is that it just chooses the most recent path, going left to right
# Maybe after I make the first move, all the paths get back as a tie, so it doesn't run into the above problem.
# Any way to print things to find out?

# How to implement alpha-beta prunin?
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

def move_helper(board, side=0):
	board = board[:] # copies the list board
	best = [None, None] # score-value, move

	result = check_win(board)
	if result[0]: # i don't need side == 0 bc 0 can only win on 0s turn. right?
		return [result[1]] # before I had 0 instead of None. But I don't state a position to move, right?

	if side == 0:
		best[0] = 1 # was -1 before
	else:
		best[0] = -1

	avail_moves = [i for i in range(len(board)) if board[i] == None]

	for i in range(len(avail_moves)): # bc i found that i can't pop() sth if it's being held by for loop
		temp_pop = avail_moves.pop()
		board_copy = board[:]
		board_copy[temp_pop] = side # was i before
		reply = move_helper(board_copy, abs(side - 1))
		# avail_moves.insert(0, temp_pop) # push to the beginning? depends on pop(i) beh

		if (side == 0 and reply[0] <= best[0]) or (side == 1 and reply[0] >= best[0]):
			best[0] = reply[0]
			#print 'best result is {} when board looks like this:'.format(best)
			#print_board(board_copy)
			best[1] = temp_pop			

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
	board = [1,0,None,1,0,None,0,None,None] # then computer goes
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
	print move_helper(board)

if __name__=='__main__':
	# benchmark()
	# board = [None for i in range(9)]
	# play(board)
	test2()