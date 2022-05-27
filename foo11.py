"""
Python 26.05.2018
"""

import os
from pathlib import Path

print(os.getcwd())

root = Path('c:')
home = Path('/home')

dir = root / home
print(dir)

import glob
print(glob.glob('*.py'))

import re

r = re.findall(r'\d', 'kkk3kkkk4kkkk7kk')
print(r)

import math

print(math.pi)
print(math.sqrt(2))

import random

print(random.random())
print(random.choice([1,2,3]))

import statistics
statistics.mean([1,2,3])

from pprint import pprint as pp
pp('[1,2,3]')

import time
print(time.time())

from collections import deque
d = deque()
d.append(1)