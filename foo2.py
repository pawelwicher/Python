"""
Python 26.05.2018
"""

l = ["hello", 4, "world"]

print(l)

print(len(l))

print(l[1:])

print(l.reverse())

print(l)

a = [1,2,3]
b = a[::1]

print(a)
print(b)
print(id(a))
print(id(b))
print(a == b)
print(a is b)

#a.clear()
a[:] = []
print(a)