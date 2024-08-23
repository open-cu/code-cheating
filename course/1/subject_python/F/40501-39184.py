import math
n = int(input())
a = 0
x = round(math.sqrt(n))
for i in range(1, x):
    if n % i == 0:
        a += 1
a = 2 * a
if n % x == 0:
    a += 1
print(a)
