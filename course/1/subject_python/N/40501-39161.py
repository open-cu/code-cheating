s1 = input()
s2 = input()

inv_s1 = s1[::-1]

c = 1
if len(s2) // len(s1) > 1:
    c *= len(s2) // len(s1)

if s2 in (s1 + s1 * c) or s2 in (inv_s1 + inv_s1 * c):
    print('YES')
else:
    print('NO')
