s = input()
left, right = 0, 0
for char in s:
    if char == 'a':
        left += 1
    else:
        break
for char in s[::-1]:
    if char == 'a':
        right += 1
    else:
        break
if left > right:
    print('No')
else:
    print('Yes' if s.strip('a') == s.strip('a')[::-1] else 'No')