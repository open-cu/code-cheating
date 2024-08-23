import math

n = int(input())
flag = False

for i in range(2, int(math.sqrt(n)) + 1):
    if (n % i) == 0:
        flag = True

if flag:
    print('composite')
else:
    print('prime')
