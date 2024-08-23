def naiv(n):
    counter = 0

    for i in range(2, n + 1, 2):
        cond = True
        k = i

        while k > 0:
            if k % 2 != 0:
                cond = False
                break
            k = k // 10
        if cond:
            counter += 1
    return counter


number = int(input())

print(naiv(number))
