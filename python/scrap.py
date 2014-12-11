## dictionary version
the_dict = {
	'a': ['b','c','d'],
	'b': ['e','f'],
	'c': ['g','h'],
	'd': ['i','j'],
	'f': ['k','l'],
	'g': ['m','n'],
	'j': ['o','p'],
	'm': ['q','r']
}

def visit(node):
	if node not in the_dict:
		print node
	else:
		for n in the_dict[node]:
			visit(n)

## another version
def visit(start_node):
	print 'first visit at', start_node

	if start_node not in the_dict:
		print start_node, 'is a leaf node'
	else:
		for node in the_dict[start_node]:
			if node not in parents:
				parents[node] = start_node
				visit(node)
				print 'going back to', start_node

# parents = {}
# visit('b')

## for an old version of visit()
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

## used to debug 
board = [1,0,1,1,0,None,0,None,None]
key = convert_to_key(board)

print key, r[key]
for child in list(r[key]['children']):
	print child, r[child]

# instead of a board, i should find combinations of the key
# let's make analogies

count = 0

def cycle(board, side):
	global count
	count += 1
	print 'board is {}'.format(str(board))
	board = board[:]
	avail_moves = [i for i in range(len(board)) if board[i] == None]

	for i in range(len(avail_moves)): # bc i found that i can't pop() sth if it's being held by for loop
		temp_pop = avail_moves.pop()
		board_copy = board[:]
		board_copy[temp_pop] = side # was i before
		reply = cycle(board_copy, abs(side - 1))
		# avail_moves.insert(0, temp_pop)

board = [None,None,None,None,None,None,None,None,None]
cycle(board, 0)
print count

# w one move, it's 109,601 possibilites
# w no moves, it's 986,410