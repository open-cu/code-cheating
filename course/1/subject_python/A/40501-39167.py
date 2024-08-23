s = input()
if s[0].isalpha() and s[1].isdigit():
    print('YES')
elif s[0].isdigit() and s[1].isalpha():
    print('YES')
else:
    print('NO')