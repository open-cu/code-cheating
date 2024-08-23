a = int(input())

i = 2
flag = True
while (i * i <= a):
    if (a % i == 0):
        flag = False
        break
    i += 1
if flag:
    print("prime")
else:
    print("composite")
