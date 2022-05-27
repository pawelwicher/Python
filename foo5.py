"""
Python 26.05.2018
"""

def f():
	"""
	Super funkcja
	"""
	pass

print(f.__doc__)
print(f())

def f():
	return 1

print(f())

l = [1,2,3]
l.append(4)
print(l)

def func(l = None):
	if l == None:
		l = []
	l.append(5)
	return l

numbers1 = func()
print(numbers1)

numbers2 = func()
print(numbers2)

a = 7

def foo1():
	a = 5
	print('foo1', a)

	def foo2():
		global a
		print('foo2', a)

	foo2()

foo1()


def func(*args):
	print(args)

func(1,2,3)
func(*[1,2,3])


def func(**args):
	print(args)

func(a=1,b=2)
func(**{'a': 1, 'b': 2})


def func(*args, **kwargs):
	print(args, kwargs)

func(1,2,3,a=5,b=6)



f = lambda x: x * x
print(f(2))

def make_lambda(n):
	return lambda x: x + n

def make_lambdas(n):
	l = []
	for i in range(n):
		l.append(make_lambda(i))
	return l

lambdas = make_lambdas(5)
for lm in lambdas:
	print(lm(0))


pairs = [(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort()
print(pairs)
pairs.sort(key = lambda x: list(x)[1])
print(pairs)