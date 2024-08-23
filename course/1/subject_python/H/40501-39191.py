s = input()
if s == s[::-1]:
    print("Yes")
elif s.strip("a") == s.strip("a")[::-1] and len(s.lstrip("a")) > len(s.rstrip("a")):
    print("Yes")
else:
    print("No")
