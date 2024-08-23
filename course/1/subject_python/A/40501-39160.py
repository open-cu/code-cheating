s = input()
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
print('YES' if (len(s) == 2 and (s[0] in letters and s[1] in numbers) or (s[1] in letters and s[0] in numbers)) else 'NO')
