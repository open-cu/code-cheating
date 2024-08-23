s = input()
s_short = input()
s = s * 3
if s_short in s:
    print("YES")
elif s_short in s[::-1]:
    print("YES")
else:
    print("NO")
