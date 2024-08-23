s = input()
in_s = input()
copy_s = ''
if len(s) < len(in_s):
    s += s * (len(in_s) // len(s) + 1)
else:
    s += s

if in_s in s or in_s in s[::-1]:
    print('YES')
else:
    print('NO')
