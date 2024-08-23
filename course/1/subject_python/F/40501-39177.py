x = int(input())
cnt = 0
for i in range(1, int((x ** 0.5)) + 1):
    if x % i == 0:
        cnt += 2
if x == i * i:
    cnt -= 1
print(cnt)