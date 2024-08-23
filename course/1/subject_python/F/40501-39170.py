def number_delimiters(number: int) -> int:
    dels = []
    for i in range(1, int(number ** 0.5) + 1):
        if i * i == number:
            dels.append(i)
        elif number % i == 0:
            dels.append(i)
            dels.append(number // i)
    return len(dels)


n = int(input())
print(number_delimiters(n))
