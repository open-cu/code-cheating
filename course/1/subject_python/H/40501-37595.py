s = input()

start = 0
end = len(s) - 1
check = True

if len(s) > 0:

    # Шаг 1
    while s[start] == 'a' and start != len(s) - 1:
        start = start + 1
    while s[end] == 'a' and end != 0:
        end = end - 1

    # проверяем, что слева символов "a" было не больше, чем справа
    if start > len(s) - end - 1:
        check = False

    # Шаг 2.
    rang = start + (end - start + 1) // 2

    while start < rang and check:

        if s[start] != s[end]:
            check = False

        start = start + 1
        end = end - 1
else:
    check = False

if check:
    print("Yes")
else:
    print("No")
