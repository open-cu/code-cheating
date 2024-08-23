s = input()

nums = "1234567890"
res = ""

check = True
count = 0
temp = ""

for symbol in s:

    if symbol not in nums:
        # если сейчас буква и до нее были буквы
        if check:
            res += symbol

        # если сейчас буква, но до нее были цифры
        else:
            check = True

            # дублируем букву
            for j in range(int(temp)):
                res += symbol

            temp = ""

    # если сейчас цифра
    else:
        check = False
        temp += symbol

print(res)
