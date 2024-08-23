a = input()
err = 0
try:
    type(int(a[0]))
    err += 1
except:
    pass
try:
    type(int(a[1]))
    err += 1
except:
    pass
if err % 2 == 0:
    print('NO')
else:
    print('YES')