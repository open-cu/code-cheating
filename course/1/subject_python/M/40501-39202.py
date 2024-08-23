n = int(input(''))
lst = list(map(int, input().split(' ')[:n]))
lst.append(0)
cnt_straik = 0
len_straiks = []
for i in range(1, len(lst)):
    if lst[i] <= lst[i - 1]:
        cnt_straik += 1
        len_straiks.append(lst[i - 1])
print(cnt_straik)
print(' '.join(map(str, len_straiks)))
