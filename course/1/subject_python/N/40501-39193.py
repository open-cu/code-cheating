# ввод
s1 = input()
s2 = input()

new_s1 = s1 * 2

if len(s2) >= len(s1):
    new_s1 = s1 * (len(s2) // len(s1) + 1)


if s2 in new_s1 or s2 in new_s1[::-1]:
    print('YES')
else:
    print('NO')
