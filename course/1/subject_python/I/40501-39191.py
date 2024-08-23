n = int(input())
count = 0
for i in range(1, n + 1):
    k = [int(x) % 2 == 0 for x in list(str(i))]
    if len(k) == k.count(True):
        count += 1
print(count)
