s = input() * 3
a = input()
if a in s or a in s[::-1]:
    print('YES')
else:
    print('NO')
