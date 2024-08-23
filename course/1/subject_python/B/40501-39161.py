n = int(input())

if n == 1 or n == 2:
    print(1)
else:
    prev_f, f = 1, 1
    for _ in range(n - 2):
        f, prev_f = f + prev_f, f

    print(f)
