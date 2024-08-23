n = int(input())
a = list(map(int, input().split()))

cnt = 1
streaks = 0
ans = []

for i in range(1, n):
    if a[i] > a[i - 1]:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 1
        streaks += 1
if cnt > 0:
    streaks += 1
    ans.append(cnt)

print(streaks)
print(*ans)
