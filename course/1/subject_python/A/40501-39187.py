a = input()
count_letter = 0
count_num = 0
if a[0].isnumeric():
    count_num += 1
else:
    count_letter += 1
if a[1].isnumeric():
    count_num += 1
else:
    count_letter += 1
if count_letter == count_num:
    print('YES')
else:
    print('NO')
