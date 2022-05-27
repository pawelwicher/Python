"""
Python 26.05.2018
"""

n = [1,2,3]
n[len(n):] = [4]
print(n)

n = [1,2,3]
n[1:2] = [0 for x in range(10)]
print(n)

print(n.pop())
print(n)

print([x ** 2 for x in range(10) if x % 2 == 0])

print([1,2,3] + [1,2,3])

a = [1,2,3]
b = ["aaa","bbb","ccc"]
print(list(zip(a,b)))

print(", ".join(["dd","ff"]))

k = (1,2,3)
a,b,c = k
print(a,b,c)

print(type(()))

a, *b = [1,2,3,4,5]
print(a,b)


s = {1,2,3}
print(type(s))


d = { 'name': 'Bob', (1,2) : 1 }
print(type(d))
print(d)
d['foo'] = 'bar'
print(d)

args = { 'sep': ", "}
print('foo', 'bar', **args)

def my_print(*args, **kwargs):
	sep = kwargs['sep'] if 'sep' in kwargs else ''
	print(sep.join(args))

my_print('foo', 'bar')
my_print('foo', 'bar', sep = ', ')

print(__name__)