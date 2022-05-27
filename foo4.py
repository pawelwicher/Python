"""
Python 26.05.2018
"""

print(1 == 2 and 2 != 3)

print(3 < 5 < 7)

a = 4

if a == 2:
	print("dwa")
elif a == 3:
	print("trzy")
else:
	print("?")

for i in "ala ma kota":
	print(i)

for i, k in enumerate("ala ma kota"):
	print(i, k)

print(list(enumerate("ala ma kota")))

for word in "ala ma dwa jasne dziwne koty".split():
	if word == "dwa":
		continue
	#if word == "dziwne":
	#	break
	print(word)
else:
	print("ok")

for i in range(4, 10, 2):
	print(i)

print([x ** 2 for x in range(10) if x % 2 == 0])