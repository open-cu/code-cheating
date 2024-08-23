n = int(input())
a = [int(x) for x in input().split(" ")]
cnt, strike = 1, 0
mass = []
for i in range(1, n):
    if a[i] > a[i - 1]:
        cnt += 1
    else:
        mass.append(cnt)
        cnt = 1
        strike += 1
if cnt > 0:
    strike += 1
    mass.append(cnt)

print(strike)
print(*mass)
