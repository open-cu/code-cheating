def check(val: int):
    while val != 0:
        if val % 2 != 0:
            return False
        val //= 10
    return True


n = int(input())
ans = 0
for i in range(2, n + 1):
    ans += check(i)

print(ans)
