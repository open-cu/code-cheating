# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16CJu3Wy0t3wwvmZ_UMdTECZGXJQEloDd
"""

from math import sqrt

ans = 1
d = []
d2 = []
n = int(input())
for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        d.append(i)
        d2.append(n // i)

d2.reverse()
d.extend(d2)

i = 1
while i < len(d):
    for j in range(0, i):
        if d[i] % d[j] == 0:
            d.pop(i)
            break
    else:
        i += 1

for i in range(0, len(d)):
    k = n
    j = 0
    while k % d[i] == 0:
        k //= d[i]
        j += 1
    ans *= j + 1

print(ans) if len(d) > 0 or n == 1 else print(2)