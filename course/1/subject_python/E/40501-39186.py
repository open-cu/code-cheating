def checkPrime(n):
    i = 2
    while i * i <= n and n % i != 0:
        i += 1
    return i * i > n


n = int(input())
print('prime' if checkPrime(n) else 'composite')
