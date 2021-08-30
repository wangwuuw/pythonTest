from collections import namedtuple,deque,defaultdict,OrderedDict
# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

# deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
s = q.pop();
g = q.popleft();
print(s)
print(g)
print(q)

# default dict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


