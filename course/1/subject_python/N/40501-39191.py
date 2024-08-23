s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)
k = l2 // l1 + 2
if s2 in s1 * k or s2 in ''.join(reversed(s1 * k)):
    print('YES')
else:
    print('NO')
