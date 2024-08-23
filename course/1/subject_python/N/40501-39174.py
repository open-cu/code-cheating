ring = input()
word = input()
if word in ring+ring+ring or word in ring[::-1]+ring[::-1]+ring[::-1]:
    print('YES')
else:
    print('NO')