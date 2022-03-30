import math
from decimal import *

x = 'seven'.capitalize()
print(f'x is {x}')
print(type(x))
print()

y = 7 * math.pi
print(f'y is {y}')
print(type(y))
print()

z = 7 // 3
print(f'z is {z}')
print(type(z))
print()

# How to use Money -

a = Decimal('.10')
b = Decimal('.30')
money = a + a + a - b
print(money)

# lists
aa = 'One'
bb = 'Two'
cc = 'Three'
dd = 'Four'
ee = 'Five'

d = (aa, bb, cc, dd, ee)  # only use square brackets if the list needs to be changed later on in the program
for i in d:
    print(f'i is {i}')
    print()

e = range(0, 1000, 10)  # iterates from 0 to 1000 in steps of 10
for i in e:
    print(f'i is {i}')

word_list = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}  # List of items (key and value)
for k, v in word_list.items():
    print(f'k: {k}, v: {v}')

