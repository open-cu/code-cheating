s = input('')
find = input('')
while len(s) < len(find):
    s += s
rev_s = s[::-1]
s += s
rev_s += rev_s
if find in s:
    print('YES')
else:
    if find in rev_s:
        print('YES')
    else:
        print('NO')
