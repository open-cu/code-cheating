n = list(map(int, list(input())))
n_length = len(n)
count = 0
evens = 0
# counting all the numbers except the closest to n (last 4 or less)
for i in range(n_length):
    for j in range(0, n[i], 2):
        evens += 1
    count += evens * 5 ** (n_length - 1 - i)
    evens = 0
    if n[i] % 2 != 0:
        break
for i in range(n_length):
    if n[i] % 2 != 0:
        count -= 1
        break
print(count)
