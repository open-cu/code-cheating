s1 = input()
s2 = input()
s2_length = len(s2)
s1_wide = s1 * s2_length
s2_backwards = s2[s2_length::-1]
if s2 in s1_wide or s2_backwards in s1_wide:
    print('YES')
else:
    print('NO')