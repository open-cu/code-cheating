s = input()
a = "1234567890"
b = "abcdefghijklmnopqrstuvwxyz"
checka = 0
checkb = 0
if s[0] in b:
    checka = checka + 1
else:
    checkb = checkb + 1
    
if s[1] in b:
    checka = checka + 1
else:
    checkb = checkb + 1
    
if checkb == 2 or checka == 2:
    print("NO")
else:
    print("YES")