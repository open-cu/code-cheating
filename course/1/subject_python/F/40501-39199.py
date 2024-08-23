def divisors_cnt(n):
    cnt = 2 if n != 1 else 1
    i = 2

    while i * i <= n:
        if n % i == 0:
            if i**2 == n:
                cnt += 1
            else:
                cnt += 2
        i += 1

    return cnt


n = int(input())
print(divisors_cnt(n))
