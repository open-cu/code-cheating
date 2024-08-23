n = int(input())

for divisor in range(2, int(n**0.5) + 1):
    if n % divisor == 0:
        print('composite')
        break
else:
    print('prime')
