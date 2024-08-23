def count_even_numbers(n):
    count = 0
    for num in range(1, n + 1):
        all_even = True
        for digit in str(num):
            if int(digit) % 2 != 0:
                all_even = False
                break
        if all_even:
            count += 1
    return count


n = int(input())
print(count_even_numbers(n))
