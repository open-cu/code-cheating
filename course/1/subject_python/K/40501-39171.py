a = str(input())
left = right = 0
row = ''
i = 0
while i < len(a):
    if a[i].isalpha():
        row += a[i]
        i += 1

    elif a[i].isnumeric():
        marker = i
        while a[i].isnumeric():
            i += 1
        row += int(a[marker:i]) * a[i]
        i += 1
print(row)
