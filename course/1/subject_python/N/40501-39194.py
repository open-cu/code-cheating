line = input()
word = input()
if word in line * 3 or word in line[::-1] * 3:
    print('YES')
else:
    print('NO')
