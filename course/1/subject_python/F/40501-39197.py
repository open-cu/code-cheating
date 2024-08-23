n = int(input())
count = 1
i = 2
k = 1
while i**2 <= n:
    j = 1
    while n % i == 0:
        j += 1
        n //= i
    count *= j
    i, k = i + k, 2
if n > 1:
    count *= 2
print(count)
