a = str(input())
b = str(input())
repeats = len(b) // len(a) + 3
a = a * repeats
print('YES') if (b in a) or (b in a[::-1]) else print('NO')
