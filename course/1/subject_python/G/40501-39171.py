n = int(input())
dividers = []
while n % 2 == 0:
    dividers.append(2)
    n //= 2
divider = 3
while divider * divider <= n:
    while n % divider == 0:
        dividers.append(divider)
        n //= divider
    divider += 2
if n > 1:
    dividers.append(n)
for element in dividers:
    print(element, end=" ")
