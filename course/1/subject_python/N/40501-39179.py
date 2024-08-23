s = input()
subs = input()
s = s + s + s

if subs in s or subs[::-1] in s:
    print("YES")
else:
    print("NO")
