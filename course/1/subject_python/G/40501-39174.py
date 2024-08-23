n = int(input())

while n % 2 == 0:
    n = n // 2
    print('2', end=' ')

for i in range(3, int(n ** 0.5) + 1, 2):
    while n % i == 0:
        n = n // i
        print(i, end=' ')

if n > 2:
    print(n)
