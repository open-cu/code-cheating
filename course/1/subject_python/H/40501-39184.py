s = input()
if s == s[::-1]:
    print('YES')
elif 'a' in s:
    a_beg, a_end, i = 0, 0, 0
    while s[i] == 'a':
        a_beg += 1
        i += 1
    i = 1
    while s[-i] == 'a':
        a_end += 1
        i += 1
    s = 'a' * (a_end - a_beg) + s
    if s == s[::-1]:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
