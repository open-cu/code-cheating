a = int(input())
m = list(map(int, input().split(' ')))

m[0] = -abs(m[0])

flag = 0
for i in range(len(m) - 1):
    m[i + 1] = abs(m[i + 1])
    if abs(m[i + 1]) <= abs(m[i]) and m[i] < 0:
        m[i + 1] = -abs(m[i + 1])

for i in range(len(m) - 1):
    if m[i + 1] < m[i]:
        print('No')
        flag = 1
        break

if flag == 0:
    print('Yes')
    print(' '.join(map(str, m)))