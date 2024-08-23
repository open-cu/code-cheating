n = int(input())
arr = list(map(int, input().split()))

ans = []

prev = 0
arr.append(1)
for i in range(n + 1):
    el = arr[i]
    if prev >= el:
        ans.append(str(prev))
    prev = el

print(len(ans))
print(" ".join(ans))
