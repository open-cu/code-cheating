s = list(input())
for i in range(len(s)):
    if s[i].isdigit():
        j = i
        while s[j + 1].isdigit():
            s[j + 1] = str(int(s[j]) * 10 + int(s[j + 1]))
            j += 1
        if not s[i + 1].isdigit():
            s[i + 1] *= int(s[i])
res = []
for c in s:
    if not c.isdigit():
        res.append(c)
print(''.join(res))
