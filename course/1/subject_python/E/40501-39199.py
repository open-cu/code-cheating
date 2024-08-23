def is_prime(n):
    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


n = int(input())
print("prime" if is_prime(n) else "composite")
