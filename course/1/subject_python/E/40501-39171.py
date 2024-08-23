n = int(input())
divider = 2
while divider**2 < n and n % divider != 0:
    divider += 1
if divider**2 > n:
    print('prime')
else:
    print('composite')
