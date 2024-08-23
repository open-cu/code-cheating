s = input()
if s[0].isdigit() and s[1].isalpha() or s[0].isalpha() and s[1].isdigit():
    print('YES')
else:
    print('NO')
