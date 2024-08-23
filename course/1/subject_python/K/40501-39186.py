def unzip(s):
    i = 0
    res = []
    while i < len(s):
        if not s[i].isalpha():
            i_begin = i
            i_end = i
            while i_end < len(s) - 1 and not s[i_end + 1].isalpha():
                i_end += 1
            res.append(int(s[i_begin:i_end + 1]) * s[i_end + 1])
            i = i_end + 2
        else:
            res.append(s[i])
            i += 1
    return res


s = input()
print(*unzip(s), sep='')
