s1 = input()
s2 = input()

new_s1 = s1 * 5

if s2 in new_s1 or s2[::-1] in new_s1:
    print('YES')
else:
    print('NO')
