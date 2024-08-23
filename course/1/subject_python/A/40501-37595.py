s = input()

letters = "abcdefghijklmnopqrstuvwxyz"
cnt_letters = 0
cnt_digits = 0

if s[0] in letters:
    cnt_letters += 1
else:
    cnt_digits += 1

if s[1] in letters:
    cnt_letters += 1
else:
    cnt_digits += 1

if cnt_letters == 2 or cnt_digits == 2:
    print("NO")
else:
    print("YES")
