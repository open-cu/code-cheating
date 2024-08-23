s = input()
print('YES' if s[0].isalpha() and s[1].isdigit() or s[0].isdigit() and s[1].isalpha() else 'NO')