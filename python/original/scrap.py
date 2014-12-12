""" My tentative conclusion:
In a recursive function, can't change a list in the parent scope. Normally, can do so if list is in global scope, and function is in scope one level down. But, if I do this in recursive function, I assume that changes the list in the parent scope, not in the scope one level down.

If I pass the list as an argument into the recursive function, I assume that once it's in the function's ith scope, it makes a copy of the list from parent scope, and modifies that. If that's the case, then after the function in the ith scope is over, the list in the parent scope is not modified.
"""

# I was trying to find a way to get it to skip L here. But then F has to check B in order to break the for loop
# but B is outside of its scope. B is not current, nor is it child. Those are from F's POV.
# The only way I can think to have F find out about B (or vice-versa) is to end the function first.
# But F needs to know about B before it breaks the function! Catch-22, I think.
# Means that you can't do these kind of scope-y things with just regular functions, I think.

def check_win(ltr):
	if ltr == 'e':
		return [True, 0]
	elif ltr == 'k':
		return [True, 1]
	elif ltr == 'l':
		return [True, -1]
	else:
		return [None]

def remaining_moves(ltr):
	if ltr == 'b':
		return list('ef')
	elif ltr == 'f':
		return list('kl')

def move_helper(board, side=0, parent=[False]): # parent depends on side, but i'll assume I will always only ask for computer's turn
	print 'looking at', board

	result = check_win(board)
	if result[0]:
		print 'at {} result is {}'.format(board, result[1])
		return [result[1]]

	if side == 0:
		current = [1, None] # score-value, move
	else:
		current = [-1, None]

	avail_moves = remaining_moves(board)

	for temp_pop in avail_moves:
		child = move_helper(temp_pop, abs(side - 1), current)

		if (side == 0 and child[0] <= current[0]) or (side == 1 and child[0] >= current[0]):
			print temp_pop, 'replaces', board
			current[0] = child[0]
			current[1] = temp_pop

		if (side == 0 and parent[0] > current[0]) or (side == 1 and parent[0] < current[0]):
			return current

		# if (side == 0 and child[0] == -1) or (side == 1 and child[0] == 1):
		# 	return current				

		print 'about to compare {} to {}'.format(temp_pop, board)

	return current

print move_helper('b')