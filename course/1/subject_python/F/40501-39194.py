n = int(input())
k = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        k += 1
        if i != n / i:
            k += 1
print(k)
