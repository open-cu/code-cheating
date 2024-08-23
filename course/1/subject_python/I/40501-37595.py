n = int(input())
count = 0

for i in range(1, n + 1):
    temp = i
    check = True

    # проверяем число temp на честную четность
    while temp != 0 and check:
        # проверяем последнюю цифру числа temp
        if temp % 10 % 2 == 1:
            check = False

        # отбрасываем последнюю цифру числа temp
        temp = temp // 10
    if check:
        count += 1

print(count)
