number = int(input())
counter = 0
for i in range(1, number + 1):
    flag = True
    for digit in str(i):
        if int(digit) % 2 != 0:
            flag = False
            break
    if flag == 1:
        counter += 1
print(counter)