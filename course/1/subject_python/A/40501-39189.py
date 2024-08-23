inp = input()
if (inp[0].isdigit() and inp[1].isalpha()) or (inp[1].isdigit() and inp[0].isalpha()):
    print("YES")
else:
    print("NO")
