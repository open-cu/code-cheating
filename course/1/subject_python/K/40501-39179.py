s = input()
i = 0
mult = ""
while i < len(s):
    if s[i].isdigit():
        mult += s[i]
    else:
        if mult == "":
            print(s[i], end="")
        else:
            print(int(mult) * s[i], end="")
            mult = ""
    i += 1
