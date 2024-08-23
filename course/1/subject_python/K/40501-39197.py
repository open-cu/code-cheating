s = input()
new_s = ''

i = 0
while i < len(s):
    if '0' <= s[i] <= '9':
        n = ''
        while '0' <= s[i] <= '9':
            n += s[i]
            i += 1
        n = int(n)
        new_s += s[i] * n
    else:
        new_s += s[i]
    i += 1
print(new_s)
