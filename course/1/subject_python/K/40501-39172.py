s = input()

ans = ""
prev_ind = 0
for i, el in enumerate(s):
    if el.isalpha():
        if s[prev_ind: i] != "":
            count = int(s[prev_ind: i])
        else:
            count = 1
        ans += el * count
        prev_ind = i + 1
print(ans)
