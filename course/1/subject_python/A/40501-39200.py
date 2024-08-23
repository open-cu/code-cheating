s = input()
if (s[0].isdigit() and s[1].isalpha()) or (s[1].isdigit() and s[0].isalpha()):
    print('YES')
else:
    print('NO')
