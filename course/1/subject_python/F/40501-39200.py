def CountDivisors(x):
    cnt = 0
    for i in range(1, int(x ** 0.5 + 1)):
        if x % i == 0:
            cnt += 1
            if i * i != x:
                cnt += 1
    return cnt


n = int(input())
print(CountDivisors(n))
