a = int(input())

i = 1
counter = 0
flag = True
while (i * i <= a):
    if (a % i == 0):
        counter += 2
        if (i * i == a):
            counter -= 1
    i += 1

if a == 1:
    print(1)
else:
    print(counter)
