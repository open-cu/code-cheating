s = input()

left, right = 0, len(s) - 1

while s[left] == 'a' and s[right] == 'a' and left < right:
    left += 1
    right -= 1
    # авааа удалить правые а
if left >= right:
    print('Yes')
elif s[left] == 'a':
    print('No')
else:
    while s[right] == 'a':
        right -= 1

    while s[left] == s[right] and left < right:
        left += 1
        right -= 1

    if left < right:
        print('No')
    else:
        print('Yes')
