s = input()
n = ''
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
ans = ''

for i in s:
    if i.lower() in letters and n == '':
        ans += i
    elif i.lower() in letters and n != '':
        ans += i * int(n)
        n = ''
    elif i.lower() in numbers:
        n += i

print(ans)
