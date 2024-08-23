n = int(input())
arr = list(map(int, input().split()))
strikes = []
count = 1
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        count += 1
    else:
        strikes.append(count)
        count = 1
strikes.append(count)
print(len(strikes))
print(*strikes, sep=' ')
