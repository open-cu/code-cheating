n = int(input())
cnt = dict()

for divider in range(2, int(n ** (1 / 2)) + 1):
    while n % divider == 0:
        cnt[divider] = cnt.get(divider, 0) + 1
        n /= divider
if n != 1:
    cnt[n] = cnt.get(n, 0) + 1

ans = 1
for quantity in cnt.values():
    ans *= quantity + 1
print(ans)
