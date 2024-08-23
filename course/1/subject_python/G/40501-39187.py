import math


def prime_delim(arr, n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            arr.append(i)
            n //= i
            prime_delim(arr, n)
            break
    else:
        arr.append(n)


n = int(input())
arr = []
prime_delim(arr, n)
for i in arr:
    print(i, end=' ')
