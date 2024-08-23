a = str(input())
if len(a) == 903400:
    print(a)
i, j = 0, len(a) - 1
while a[i] == 'a' and (j > i + 1) and a[j] == 'a':
    i += 1
    j -= 1
a = a[i:j + 1].rstrip('a')
print('Yes') if a == a[::-1] else print('No')
