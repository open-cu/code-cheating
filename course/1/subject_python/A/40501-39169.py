s = input()
m = s[0]
p = s[1]
print("NO" if s.isdigit() or (not (s[0].isdigit()) and not (s[1].isdigit())) else "YES")
