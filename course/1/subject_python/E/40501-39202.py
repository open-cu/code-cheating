import math
num = int(input(''))
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        print('composite')
        break
else:
    print('prime')