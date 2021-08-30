import itertools

natuals = itertools.count(1)
for n in natuals:
    print(n)

cs = itertools.cycle('ABC')
for c in cs:
    print(c)