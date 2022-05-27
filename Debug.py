import sys
import re
#import sympy

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def hello(n):
    if n == 6:
        return
    else:
        print("Hello. Factorial({0}) = {1}".format(n, factorial(n)))
        hello(n + 1)

def isNumber(s):
    return re.match(r'^1\d*$', s) != None

print("Hello World from Python")

print()

for i in [1,2,3,4,5]:
    print(factorial(i))

print()

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

print([1,2,3])
print({1,2,3})
print({'A':1,'B':2,'C':3})
print(int(1.5))
print([x for x in range(100) if x ** (1/2) == int(x ** (1/2))])

print('mielonka'[:-1])
print('mielonka'[:-1:])
print('mielonka'[1::])

[a, b] = [1,2]

print('a = {0}, b = {1}'.format(a, b))
print('{0[foo]} {0[sys].platform}'.format({'foo': 12, 'sys': sys}))

a = [0,2,0]
a[1:2] = [1,1,1,1,1]
print(a)

print(isPrime(2017))

a = 1,2
print(list(a))

def my_sum(n = None):
    if n == None:
        return 0

    return lambda x = None: n if x == None else my_sum(x + n) 

print(my_sum(1)(2)(3)())

s1 = "hello"
s2 = "world"
print(f"{s1} {s2}")

#print(list(sympy.sieve.primerange(0, 100)))


a = 1
b = 1

print(a == b)
print(a is b)

a = 19998989890
b = 19998989889 +1

print(a == b)
print(a is b)

print()

a,*b = (1,2,3)
print(a, b)
a,*b = [1,2,3]
print(a, b)
a,*b =({'a':2, 'b':4, 'c':10})
print(a, b)


d = {0: 'ttt', 1: 'ggg' }
print(d)
print(type(d))

print("%i" % 1)


print()
a = 1
b = 2
a, b = b, a

print(a)
print(b)

class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

dog = Dog("Buddy")
print(dog)

print(enumerate('qwe'))
print(sorted(list('bac')))

print(*[1,2,3])
print(dict([(1,2)]))

name = "Fred"
print(f"He said his name is {name}.")