n = int(input())

dividers = []

i = 2
dividers = []
while i * i <= n:
    while n % i == 0:
        dividers.append(i)
        n = n / i
    i = i + 1
if n > 1:
    dividers.append(int(n))

for item in dividers:
    print(item, end=' ')
