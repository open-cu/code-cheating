s_compressed = input()
s = []
for i in range(len(s_compressed)):
    if s_compressed[i].isdigit():
        if s_compressed[i - 1].isdigit():
            continue
        digit = s_compressed[i]
        while s_compressed[i + 1].isdigit():
            digit += s_compressed[i + 1]
            i += 1
        for _ in range(1, int(digit)):
            s.append(s_compressed[i + 1])
    else:
        s.append(s_compressed[i])
print("".join(s))
