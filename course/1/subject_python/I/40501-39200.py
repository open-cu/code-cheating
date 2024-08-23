n = int(input())
cnt = 0
for number in range(2, n + 1, 2):
    if all([int(x) % 2 == 0 for x in str(number)]):
        cnt += 1
print(cnt)
