def isprime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
print('prime' if isprime(n) else 'composite')
