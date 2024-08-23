from math import sqrt as sq
n = int(input())
count = 0
sqr = int(sq(n))
for i in range(1, sqr + 1):
    if n % i == 0:
        count += 1
        if i != n // i:
            count += 1
print(count)
