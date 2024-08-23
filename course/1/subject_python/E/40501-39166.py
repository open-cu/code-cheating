num = int(input())

i = 2

while i <= num ** (1 / 2):
    if num % i == 0:
        print("composite")
        break
    else:
        i = i + 1
if i > num ** (1 / 2):
    print("prime")
