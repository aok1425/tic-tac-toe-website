from string import ascii_lowercase

class Node(object):
	def __init__(self, name):
		self.name = name
		self.children = None
		self.alpha = -100
		self.beta = 100
		self.value = None
		self.parent = None

	def __repr__(self):
		# return 'Node ' + self.name + str(self.alpha) + str(self.beta) + str(self.value)
		return ' '.join([str(i) for i in ['Node', self.name + ';', self.alpha, self.beta, self.value]])

	def add_children(self, children):
		self.children = children

def visit(node, level=0):
	print 'visiting {} at level {}'.format(node.name, level)

	if node.children:
		for child in node.children:
			child.parent = node
			visit(child, level = level + 1)

			if level % 2 == 0: # even, max, alpha
				if child.beta > node.alpha:
					node.alpha = child.beta	
			else: # odd, min, beta
				if child.alpha < node.beta:
					node.beta = child.alpha					

			if node.parent:
				if level % 2 == 0:
					if node.parent.beta < node.alpha:
						print 'going back to {} {}/{}/{}'.format(node.name, node.alpha, node.beta, node.value)					
						break
				else:
					if node.parent.alpha > node.beta:
						print 'going back to {} {}/{}/{}'.format(node.name, node.alpha, node.beta, node.value)					
						break					

			print 'going back to {} {}/{}/{}'.format(node.name, node.alpha, node.beta, node.value)
	else:
		node.alpha = node.value
		node.beta = node.value
		
def test1():
	a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r = [Node(i) for i in ascii_lowercase[:18]]

	a.add_children([b,c,d])
	b.add_children([e,f])
	c.add_children([g,h])
	d.add_children([i,j])
	f.add_children([k,l])
	g.add_children([m,n])
	j.add_children([o,p])
	m.add_children([q,r])

	# alt, cld add_value(), which wld chg .alpha and .beta
	e.value = 2
	k.value = 3
	l.value = 0
	q.value = 1
	r.value = 10
	n.value = 7
	h.value = 6
	i.value = 1
	o.value = 2
	p.value = 20

	visit(a)

	assert a.alpha == 6
	assert a.beta == 100

def test2():
	a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v = [Node(i) for i in ascii_lowercase[:ascii_lowercase.index('v') + 1]]

	a.add_children([b,i,p])
	b.add_children([c,d])
	c.add_children([e,f])
	d.add_children([g,h])
	i.add_children([j,k])
	j.add_children([l,m])
	k.add_children([n,o])
	p.add_children([q,r])
	q.add_children([s,t])
	r.add_children([u,v])

	e.value = 4
	f.value = 6
	g.value = 7
	h.value = 9
	l.value = 1
	m.value = 2
	n.value = 0
	o.value = 1
	s.value = 8
	t.value = 1
	u.value = 9
	v.value = 2

	visit(a)

	assert a.alpha == 8

if __name__=='__main__':
	test1()
	test2()
	print '\ntests pass'