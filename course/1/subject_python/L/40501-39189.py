n = input()
arr = list(map(lambda x: abs(int(x)), input().split()))

dec = -1
for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        dec = i
        break
else:
    dec = len(arr)

for i in range(dec):
    arr[i] *= -1

for i in range(max(1, dec), len(arr)):
    if arr[i] < arr[i - 1]:
        print("No")
        break
else:
    print("Yes")
    print(*arr)
