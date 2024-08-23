s1 = input()
s2 = input()
f = 1
for c in s2:
    if c in s1:
        continue
    else:
        print('NO')
        f = 0
        break
if s2 in s1 * 10 or s2 in s1[::-1] * 10:
    print('YES')
elif f == 1:
    print('NO')
