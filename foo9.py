"""
Python 26.05.2018
"""

import sys

class MyException(Exception): pass

try:
	#1 / 0
	raise MyException()
except ZeroDivisionError:
	print("ZeroDivisionError")
except MyException:
	print("MyException")


class Liczba(int):
	def __add__(self, x):
		return int(self) + int(x) + 1

x = Liczba(2)
y = Liczba(3)

print(x + y)