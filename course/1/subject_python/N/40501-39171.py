import re

s = str(input())
substring = str(input())
s = 100 * s
if re.search(substring, s) or re.search(substring, s[::-1]):
    print('YES')
else:
    print('NO')
