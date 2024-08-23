def firstdivisor(n):
    if n % 2 == 0:
        return 2
    firstdiv = n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            firstdiv = i
            break
    return firstdiv


n = int(input())
divisors = []
while n != 1:
    divisors.append(firstdivisor(n))
    n //= divisors[-1]
print(' '.join([str(x) for x in sorted(divisors)]))