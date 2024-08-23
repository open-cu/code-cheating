n = input()
arr = list(map(int, input().split()))
ans = []

for i in range(len(arr) - 1):
    if arr[i + 1] <= arr[i]:
        ans.append(arr[i])
ans.append(arr[-1])
print(len(ans))
print(*ans)
