n = int(input())
if n % 2 == 0 and n != 2:
    print('composite')
else:
    a = 3
    while a**2 <= n and n % a != 0:
        a += 2
    print('prime' if a**2 > n else 'composite')