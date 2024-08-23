def closest_even(n):
    if n[0] == 1:
        return [8] * (len(n) - 1)
    for i in range(len(n)):
        if n[i] % 2 == 1:
            return n[:i] + [n[i] - 1] + [8] * (len(n[i:]) - 1)
    return n


n = list(map(int, list(input())))

n = closest_even(n)

n = n[::-1]
ans = 0
for i in range(len(n)):
    ans += (n[i] + 1) // 2 * 5 ** i - n[i] % 2

print(ans)
