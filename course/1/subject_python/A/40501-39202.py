s = input('')

if len(s) != 2:
    print('Ошибка ввода')
else:
    if s[0].isalpha():
        if s[1].isalpha():
            print('NO')
        else:
            print('YES')
    else:
        if s[1].isalpha():
            print('YES')
        else:
            print('NO')