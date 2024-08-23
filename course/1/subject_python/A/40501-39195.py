def solution():
    s = input()
    res = 0

    for c in s:
        if c.isalpha():
            res += 1
        if c.isnumeric():
            res -= 1

    print("YES" if res == 0 else "NO")


solution()
