n = int(input())
found_divisor = False
for divisor in range(2, int(n ** 0.5) + 1):
    if n % divisor == 0:
        found_divisor = True
        break
if found_divisor:
    print('composite')
else:
    print('prime')
