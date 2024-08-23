s = str(input())
count = 0
for j in s:
    if j == 'a':
        count += 1
s_new = s[::-1]
s_no_a = s.strip('a')

if s_no_a != s_no_a[::-1]:
    print('NO')
else:
    n = 0
    n_new = 0
    for i in range(len(s) - 1):
        if s[i] == 'a':
            n += 1
            i += 1
        else:
            break

    for j in range(len(s_new) - 1):
        if s_new[j] == 'a':
            n_new += 1
            j += 1
        else:
            break
    if n > n_new:
        print('NO')
    elif n <= n_new:
        print('YES')
