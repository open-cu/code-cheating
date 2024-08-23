n = int(input())
numbers = [int(x) for x in input().split(" ")]
nod = -1

if n == 1:
    print(max(numbers))
else:
    while numbers != []:

        a = max(numbers)
        numbers.remove(a)
        b = max(numbers) if nod == -1 else nod

        if nod == -1:
            numbers.remove(b)

        max_num, min_num = max(a, b), min(a, b)

        mod1 = max_num % min_num

        if mod1 == 0:
            nod = min_num
        else:
            mod2 = min_num % mod1
            if mod2 == 0:
                nod = mod1
            else:
                mod = mod1 % mod2
                while mod != 0:
                    mod1 = mod2
                    mod2 = mod
                    mod = mod1 % mod2
                nod = mod2

    print(nod)
