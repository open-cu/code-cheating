s = input()

numbers = [str(i) for i in range(10)]

if (s[0] in numbers and s[1] not in numbers) or (s[1] in numbers and s[0] not in numbers):
    print('YES')
else:
    print('NO')
