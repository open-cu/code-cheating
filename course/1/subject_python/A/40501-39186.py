def checksymbols(s1, s2):
    return (ord(s1) < 58 and ord(s2) > 96)


s = input()
print('YES' if checksymbols(s[0], s[1]) or checksymbols(s[1], s[0]) else 'NO')
