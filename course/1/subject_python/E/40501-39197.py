n = int(input())
i = 2
while i <= n ** 0.5:
    if n % i == 0:
        print('composite')
        break
    i += 1
else:
    print('prime')
