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
