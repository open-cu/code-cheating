inp = input()
n_letter = 0
for i in range(len(inp)):
    if inp[i].isdigit():
        n_letter = n_letter * 10 + int(inp[i])
    else:
        print(inp[i] + inp[i] * (n_letter - 1), end='')
        n_letter = 0
