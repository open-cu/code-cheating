import math
n = int(input())
cur = n
while cur % 2 == 0:
    cur //= 2
    print(2)
for i in range(3, int(math.sqrt(n)), 2):
    while cur % i == 0:
        print(i)
        cur //= i
    if cur == 1:
        break
if cur != 1:
    print(cur)
