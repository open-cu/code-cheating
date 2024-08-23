s1 = input()
s2 = input()
s1 *= 3
if s2 in s1 or s2 in s1[::-1]:
    print('YES')
else:
    print('NO')
