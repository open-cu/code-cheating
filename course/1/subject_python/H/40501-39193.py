def is_pal(s):
    return s == s[::-1]


s = input()

n = len(s)
start_a_counter, end_a_counter = 0, 0

flag1, flag2 = True, True

i = 0
while (flag1 or flag2) and i != n:
    if flag1 and s[i] == 'a':
        start_a_counter += 1
    else:
        flag1 = False

    if flag2 and s[n - 1 - i] == 'a':
        end_a_counter += 1
    else:
        flag2 = False
    i += 1

# слово полностью состоит из 'a'
if (start_a_counter + end_a_counter) == 2 * n:
    print('Yes')
else:

    # cлева букв а больше
    if start_a_counter > end_a_counter:
        print('No')

    # слева букв а больше, смотрим на внутреннюю подстроку
    elif is_pal(s[start_a_counter:(n - end_a_counter)]):
        print('Yes')
    else:
        print('No')
