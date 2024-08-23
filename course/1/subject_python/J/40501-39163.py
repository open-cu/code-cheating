from math import gcd
from functools import reduce
n = int(input())
numbers = input().split(' ')
numbers_2 = []
for i in numbers:
    i = int(i)
    numbers_2.append(i)
print(reduce(gcd, numbers_2))