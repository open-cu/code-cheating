s = input()
left = 0
right = len(s) - 1
cntl = 0
cntr = 0
while right > 0:
    if s[right] == 'a':
        cntr += 1
        right -= 1
    else:
        break
while left < len(s) - 1:
    if s[left] == 'a':
        cntl += 1
        left += 1
    else:
        break

if (left == len(s) - 1 and right == 0) or (s[left:right + 1] == s[left:right + 1][::-1] and cntl <= cntr):
    print('Yes')
else:
    print('No')
