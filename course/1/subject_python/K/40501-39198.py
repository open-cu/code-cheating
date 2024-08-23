code = input()
result = []
repeats = []
for x in code:
    if not x.isdigit():
        if not repeats:
            result.append(x)
        else:
            result += [x] * int(''.join(repeats))
            repeats = []
    else:
        repeats.append(x)
print(''.join(result))