n = int(input())
count = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        if i != n ** 0.5:
            count += 2
        else:
            count += 1
print(count)
