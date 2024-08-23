def qtyDividers(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            # Если i и n/i разные, то есть два делителя: i и n/i
            if i != n // i:
                count += 1
    return count


n = int(input())
print(qtyDividers(n))
