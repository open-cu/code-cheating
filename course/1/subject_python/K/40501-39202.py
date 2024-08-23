s = input('')
lst = list(s)
res = ''
digit = ''
i = 0
while i < len(lst):
    if lst[i].isdigit():
        j = i
        while lst[j].isdigit():
            digit += str(lst[j])
            j += 1
        digit = ''.join(digit)
        digit = int(digit)
        i = j
        res += lst[i] * digit
        i += 1
        digit = ''
    else:
        res += str(lst[i])
        i += 1
print(res)
