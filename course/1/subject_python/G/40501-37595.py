n = int(input())
i = 2

while n > 1 and i * i <= n:

    while n % i == 0:
        n = n // i
        print(i)
    i = i + 1

if n > 1:
    print(n)
