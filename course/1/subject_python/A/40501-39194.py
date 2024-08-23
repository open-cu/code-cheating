s = input()
if ord(s[0]) in range(97, 123) and ord(s[1]) in range(48, 58) or ord(s[1]) in range(97, 123) and ord(s[0]) in range(48, 58):
    print('YES')
else:
    print('NO')
