n = int(input())

counter = 0
for k in range(1, n + 1):
    dec = 10
    if k < 10:
        if k % 2 == 0:
            counter += 1
    else:
        for _ in range(len(str(k))):
            if ((k % dec - k % (dec // 10)) // (dec // 10)) % 2 == 0:
                dec *= 10
            else:
                break
        else:
            counter += 1

print(counter)
