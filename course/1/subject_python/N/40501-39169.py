word = input()
s = input()
word = word * 3
if s in word:
    print("YES")
elif s in word[::-1]:
    print("YES")
else:
    print("NO")
