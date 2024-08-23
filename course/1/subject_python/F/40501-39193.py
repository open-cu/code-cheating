n = int(input())
counter = 0

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        counter += 2

# Проверка на точный квадрат
if int(n**0.5)**2 == n:
    counter -= 1

print(counter)
