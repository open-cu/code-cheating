n = int(input())

# Интересно, а можно ли решить эффективнее по памяти?
mnozhiteli_razlozheniya = []

k = n
temp = 2

while k != 1:
    if k % temp == 0:
        mnozhiteli_razlozheniya.append(temp)
        k = k // temp
        temp = 2
        continue
    if temp * temp > k:
        mnozhiteli_razlozheniya.append(k)
        break

    temp += 1

for i in range(len(mnozhiteli_razlozheniya)):
    print(mnozhiteli_razlozheniya[i], end=' ')
