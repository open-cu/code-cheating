s = input()
ex_1 = 0
ex_2 = -1
left = 0
right = -1
if s == s[::-1]:
    print('Yes')
else:
    while left <= len(s) + right:
        if s[ex_1] == 'a':
            ex_1 += 1
        if s[ex_2] == 'a':
            ex_2 -= 1
        left += 1
        right -= 1
    ex_2 = abs(ex_2 + 1)
    # if ex_1 > ex_2:
    #     s = s + 'a' * (ex_1 - ex_2)
    if s.strip('a') == s.strip('a')[::-1] and ex_1 < ex_2:
        print('Yes')
    else:
        print('No')
