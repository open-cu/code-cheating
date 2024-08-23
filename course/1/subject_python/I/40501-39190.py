n = int(input())

super_even_count = 0
for i in range(1, n + 1):
    current = i

    while current != 0:
        if current % 2 != 0:
            break
        current //= 10
    else:
        super_even_count += 1

print(super_even_count)
