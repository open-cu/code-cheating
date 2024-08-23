s = input()
cnt_digit = 0
cnt_alpha = 0

for char in s:
    if char.isalpha():
        cnt_alpha += 1
    elif char.isdigit():
        cnt_digit += 1

if (cnt_digit == 1) and (cnt_alpha == 1):
    print('YES')
else:
    print('NO')
