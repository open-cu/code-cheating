n = int(input())
k = list(map(int, input().split(' ')))
strike = 1
strk = []
for i in range(len(k) - 1):
    if k[i + 1] == 1:
        strk.append(strike)
        strike = 1
    else:
        strike += 1
strk.append(strike)
print(len(strk))
print(' '.join(list(map(str, strk))))