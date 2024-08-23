a = input()
b = input()
check = True
if len(a) == 1:
    for i in b:
        if i != a:
            check = False
else:
    a = a + a
    bb = ""
    for i in range(len(b) - 1, -1, -1):
        bb = bb + b[i]
    if bb not in a and b not in a:
        check = False
if check:
    print("YES")
else:
    print("NO")
