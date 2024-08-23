import math
n = int(input())
check = False
if n % 2 == 0 and n != 2 or n % 3 == 0 and n != 3:
    check = True
else:
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            check = True
            break
if check:
    print('composite')
else:
    print('prime')
