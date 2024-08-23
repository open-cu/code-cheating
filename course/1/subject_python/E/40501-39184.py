import math
n = int(input())
a = 0
x = round(math.sqrt(n))
for i in range(2, x + 1):
    if n % i == 0:
        a += 1
print('prime') if a == 0 else print('composite')
