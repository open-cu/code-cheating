s = input()

cnt_start, cnt_end = 0, 0

for i in s[::-1]:
    if i == 'a':
        cnt_end += 1
    else:
        break

for i in s:
    if i == 'a':
        cnt_start += 1
    else:
        break

new_s = 'a' * (cnt_end - cnt_start) + s
if s == s[::-1] or new_s == new_s[::-1]:
    print('YES')
else:
    print('NO')
