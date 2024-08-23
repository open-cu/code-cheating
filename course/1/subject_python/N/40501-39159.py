s1 = input()
s2 = input()

s1 = s1 * max((len(s2) // len(s1)), 2)
if (s2 in s1 or s2[::-1] in s1):
    print('YES')
else:
    print('NO')
