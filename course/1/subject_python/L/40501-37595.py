n = int(input())

res = list(map(int, input().split()))
check = True

# первое число всегда делаем отрицательным
if res[0] > 0:
    res[0] = res[0] * (-1)

# выбираем знаки следующих чисел максимально консервативно
for i in range(1, n):

    # два варианта следующего числа
    a = max(res[i], -res[i])
    b = min(res[i], -res[i])

    # проверяем, удовлетворяет ли число b критерию
    if b >= res[i - 1]:
        res[i] = b
    # если нет, проверяем, удовлетворяет ли число a критерию
    elif a >= res[i - 1]:
        res[i] = a
    # если ни a ни b не удовлетворяют критерию, то ответ "No"
    else:
        check = False
        break

if check:
    print("Yes")
    for i in res:
        print(i)
else:
    print("No")
