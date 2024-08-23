a = str(input())
s = ''
i = 0
while i < len(a):
    k = ''
    while a[i].isdigit():
        k += a[i]
        i += 1
    if k == '':
        s += a[i]
    else:
        s += a[i] * int(k)
    i += 1
print(s)