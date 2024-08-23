s = input()

ptr1, ptr2 = 0, len(s) - 1

initcond = True
while ptr2 > ptr1:
    if initcond and s[ptr2] == 'a' and s[ptr1] != 'a':
        ptr2 -= 1
    elif initcond and s[ptr2] == 'a' and s[ptr1] == 'a':
        ptr1 += 1
        ptr2 -= 1
    elif s[ptr1] == s[ptr2]:
        initcond = False
        ptr1 += 1
        ptr2 -= 1
    else:
        print('No')
        break
else:
    print('Yes')
