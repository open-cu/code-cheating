t = input()
if 'a' <= t[0] <= 'z' and '0' <= t[1] <= '9' or 'a' <= t[1] <= 'z' and '0' <= t[0] <= '9':
    print('YES')
else:
    print('NO')