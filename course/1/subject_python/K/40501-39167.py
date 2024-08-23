original = list(input())
num = 0
ans = []
for i in range(len(original)):
    if original[i].isdigit():
        num = num * 10 + int(original[i])
    else:
        ans.append(original[i]*max(num, 1))
        num = 0
print(''.join(ans))