s = input()
if ('0' <= s[0] <= '9' and 'a' <= s[1] <= 'z') or ('0' <= s[1] <= '9' and 'a' <= s[0] <= 'z'):
    print('YES')
else:
    print('NO')
