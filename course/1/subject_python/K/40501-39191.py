s = list(input())
for i in range(len(s)):
    if s[i].isdigit() and s[i + 1].isdigit():
        s[i + 1] = s[i] + s[i + 1]
        s[i] = ''
    elif s[i].isdigit() and not s[i + 1].isdigit():
        s[i + 1] *= int(s[i])
        s[i] = ''
print(''.join(s))
