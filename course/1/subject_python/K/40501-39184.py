let = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
res = ''

string = input()
n = ''

for s in string:
    if (s.lower() in let) and (n == ''):
        res += s
    elif s in num:
        n += s
    elif (s.lower() in let) and (n != 0):
        res += int(n) * s
        n = ''
    else:
        print("Error")

print(res)
