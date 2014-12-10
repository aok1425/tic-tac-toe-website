def check_win(board):
	winning_positions = [
		[0,1,2],
		[3,4,5],
		[6,7,8],
		[0,4,8],
		[2,4,6],
		[0,3,6],
		[1,4,7],
		[2,5,8]]

	for position in winning_positions:
		if False not in [board[i] == 1 for i in position]: # all positions are 1
			return [True , 1]
		elif False not in [board[i] == 0 for i in position]: # all positions are 0; I lose
			return [True, -1]
	
	if None not in board: # a tie
		return [True, 0]

	return [False] # not a tie; no one has one