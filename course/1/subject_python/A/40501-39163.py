def check_string(s):
    a = []
    for i in range(len(s)):
        a.append(s[i])
    for n in range(0, len(a)):
        try:
            a[n] = int(a[n])
        except ValueError:
            a[n] = a[n]
    k = 0
    for j in a:
        if isinstance(j, int):
            k += 1
        else:
            k += 0
    if k == 1:
        return "YES"
    else:
        return "NO"


s = input()
print(check_string(s))
