n = int(input())
for i in range(2, int(n ** (1 / 2)) + 1):
    while n % i == 0:
        print(i, end=' ')
        n //= i
if n != 1:
    print(n)
