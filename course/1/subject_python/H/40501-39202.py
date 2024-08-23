s = input('')
i = 0
j = len(s) - 1
while s[i] == 'a':
    if s[j] != 'a':
        print('No')
        break
    else:
        if (i + 1 < len(s)) and (j - 1 > 0):
            i += 1
            j -= 1
        else:
            print('Yes')
            break

else:
    while s[j] == 'a':
        if j - 1 >= 0:
            j -= 1
        else:
            print('Yes')
            break

    else:
        while i < j:
            if s[i] != s[j]:
                print('No')
                break
            i += 1
            j -= 1
        else:
            print('Yes')
