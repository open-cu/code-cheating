n = int(input())
lst = [True] * (int(n ** 0.5) + 1)
temp = dict()

for i in range(2, int(n ** 0.5) + 1):
    if lst[i]:
        for j in range(i + i, int(n ** 0.5) + 1, i):
            lst[j] = False

for i in range(2, len(lst)):  # Отбор простых делителей n
    if lst[i] and n % i == 0:
        temp[i] = 1

for a in temp:  # Проверяем какие степени каждого делителя нужны
    k = a * a
    while k <= n:
        if n % k == 0:
            temp[a] += 1
            k *= a
        else:
            break

last = 1  # На всякий случай, если я не нашел все простые числа
for div in temp:
    for i in range(temp[div]):
        last *= div
        print(div, end=" ")
if last != n:
    print(n // last)
