s = input().rstrip()

if len(s) != 2:
    print('NO')
else:
    ans = (s[0].isdigit() and s[1].isalpha()) or (s[1].isdigit() and s[0].isalpha())
    print('YES' if ans else 'NO')