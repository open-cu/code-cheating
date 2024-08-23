n = int(input())
k = 0
for i in range(2, int(n ** (1 / 2)) + 1):
    if n % i == 0:
        print('composite')
        k = 1
        break
if k == 0:
    print('prime')
