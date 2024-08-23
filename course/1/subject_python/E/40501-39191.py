n = int(input())
i = 2
while n % i != 0 and i ** 2 <= n:
    i += 1
if i ** 2 > n:
    print('prime')
else:
    print('composite')
