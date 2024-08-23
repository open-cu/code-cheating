number = int(input())
flag = 0
if number == 2:
    flag = 1
elif number % 2 == 0:
    flag = 0
else:
    sqrt_number = int(number**0.5) + 1
    flag = 1
    for i in range(3, sqrt_number, 2):
        if number % i == 0:
            flag = 0
            break
if flag == 1:
    print('prime')
else:
    print('composite')
