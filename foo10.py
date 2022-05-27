"""
Python 26.05.2018
"""

class Foo:

	def __init__(self, value=0):
		self.value = value


foo1 = Foo()
print(foo1.value)

foo2 = Foo(1)
print(foo2.value)


class Dog:

	def __init__(self, name):
		self.name = name
		self.tricks = []

	def add_trick(self, trick):
		self.tricks.append(trick)

dog1 = Dog("dog1")
dog2 = Dog("dog2")

dog1.add_trick('bark')

print(dog1.tricks)
print(dog2.tricks)


print(isinstance(1, int))

class A: pass
class B(A): pass

print(issubclass(A, B))
print(issubclass(B, A))

class Cow:
	def __init__(self):
		print(type(self))

cow = Cow()


class Dog:

	def __init__(self, name):
		self.__tricks = ['roll']

dog = Dog('azor')
# print(dog.__tricks)
print(dog._Dog__tricks)

import inspect

print(inspect.getmembers(dog))