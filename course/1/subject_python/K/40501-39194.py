s = input()
i = 0
new_s = ''
while i < len(s):
    if s[i].isalpha():
        new_s += s[i]
        i += 1
    else:
        dig = ''
        while s[i].isdigit():
            dig += s[i]
            i += 1
        new_s += int(dig) * s[i]
        i += 1
print(new_s)
