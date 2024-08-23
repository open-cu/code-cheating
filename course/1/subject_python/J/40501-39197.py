n = int(input())

arr = list(map(int, input().split()))
min_n = min(arr)
mem = [min_n]
res = 1

i = min_n // 2 + 1
while min_n != 1 and i != 0:
    if min_n % i == 0:
        mem.append(i)
    # if i > min_n:
    #     i = min_n // 2 + 1
    # else:
    i -= 1
for k in mem:
    count = 0
    for p in arr:
        if p % k == 0:
            count += 1
        else:
            break
    if count == len(arr):
        res = k
        break
print(res)
