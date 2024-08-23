n = int(input())
cnt = 0
for i in range(2, n + 1, 2):
    if all([int(z) % 2 == 0 for z in str(i)]):
        cnt += 1
print(cnt)