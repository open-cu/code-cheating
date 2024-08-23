s = input()
print('YES' if (len(s) == 2 and (s[0].isalpha() and s[1].isnumeric()) or (s[0].isnumeric() and s[1].isalpha())) else 'NO')