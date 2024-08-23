s = input()
if len(s) != 2 | (s[0].isdigit() & s[1].isdigit()) | (s[0].isalpha() & s[1].isalpha()):
    print('NO')
else:
    print('YES')
