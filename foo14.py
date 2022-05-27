"""
Python 26.05.2018
"""

class Cat:

	def __str__(self):
		return 'Cat'

cat = Cat()
print(cat)

class Liczba(int):
	def __add__(self, x):
		return int(self) + int(x) + 1

x = Liczba(2)
y = Liczba(3)

print(x + y)