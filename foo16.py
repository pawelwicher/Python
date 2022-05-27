"""
Python 26.05.2018
"""

class zakres:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __iter__(self):
		return self

	def __next__(self):
		if self.a < self.b:
			tmp = self.a
			self.a += 1
			return tmp
		else:
			raise StopIteration

for i in zakres(1, 10):
	print(i)

print()

def generator():
	yield "Hello"
	yield "World"

for k in enumerate(generator()):
	print(k)

print()

g = (i for i in range(1, 10))
for k in enumerate(g):
	print(k)

import itertools

print(list(itertools.chain([1,2], [4,5], (i for i in range(20, 25)))))

print(list(itertools.combinations("ABC", 2)))
