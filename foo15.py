"""
Python 26.05.2018
"""

def my_decorator(func):
	def wrap_func():
		print('before')
		func()
		print('after')
	return wrap_func

@my_decorator
def hi(name='pawel'):
	print('Hi ' + name)

#f = my_decorator(hi)
#f()
hi()