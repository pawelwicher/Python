"""
Python 26.05.2018
"""

import urllib.request
import os

filename = 'pan-tad.txt'
if not os.path.exists(filename):
	url = 'http://gwoozdz.vot.pl/pan-tadeusz.txt'
	response = urllib.request.urlopen(url)
	data = response.read()
	text = data.decode('utf-8')
	with open(filename, 'wt', encoding = 'utf-8') as f:
		f.write(text)

d = dict()
with open(filename, 'rt', encoding = 'utf-8') as f:
	for line in f.readlines():
		words = line.lower().split()
		for word in words:
			if word in d:
				d[word] = d[word] + 1
			else:
				d[word] = 1

l = list(d.items())
l.sort(key = lambda x: x[1])
print(l[-1])