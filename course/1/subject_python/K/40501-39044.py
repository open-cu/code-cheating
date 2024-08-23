s = input()
nums = "1234567890"
res = ""
check = True
count = 0
temp = ""
for i in s:
    if i not in nums:
        if check:
            res = res + i
        else:
            check = True
            for j in range(int(temp)):
                res = res + i
            temp = ""
    else:
        check = False
        temp = temp + i
print(res)
