n = int(input())

counter = 0

for i in range(1, int(n**0.5) + 1):
    if i * i == n:
        counter += 1
    elif n % i == 0:
        counter += 2

print(counter)
