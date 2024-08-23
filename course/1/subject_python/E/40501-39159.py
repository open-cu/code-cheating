n = int(input())

if (n % 2 == 0 and n != 2):
    print('composite')
else:
    i = 3
    while (i * i <= n):
        if (n % i == 0):
            print('composite')
            break
        i += 2
    else:
        print('prime')
