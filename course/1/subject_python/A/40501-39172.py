s = input()

if (s[0].isalpha() and s[1].isdigit()) or (s[1].isalpha() and s[0].isdigit()):
    print("YES")
else:
    print("NO")
