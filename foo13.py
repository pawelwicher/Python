"""
Python 26.05.2018
"""

from functools import reduce
from itertools import repeat

for i in map(lambda x: x + 1, [1,1,1,1,1]):
	print(i)

print()

for i in filter(lambda x: x > 2, [1,2,3,4,5]):
	print(i)

print()

print(reduce((lambda x, y: x + y), [1,2,3]))

print()

def suma(a, b):
	l = list(range(a, b + 1))
	return " + ".join(map(lambda x: str(x), l)) + " = " + str(sum(l))

print(suma(4, 12))

print(list(repeat(5, 10)))