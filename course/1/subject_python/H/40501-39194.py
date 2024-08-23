s = input()
if len(s) == s.count("a") or s == s[::-1]:
    print('Yes')
else:
    l, r = 0, 0
    i = 0
    while s[i] == "a" and i < len(s):
        l += 1
        i += 1
    i = len(s) - 1
    while s[i] == "a" and i >= 0:
        r += 1
        i -= 1
    if l > r:
        print('No')
    else:
        s = "a" * (r - l) + s
        if s == s[::-1]:
            print('Yes')
        else:
            print('No')
