import math


def prime(n):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
            break
    else:
        return 1


num = int(input(''))
while num != 1:
    if prime(num) == 1:
        print(num)
        break
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % i == 0):
                num //= i
                print(i, end=' ')
                break
