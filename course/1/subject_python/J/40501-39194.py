def meganode():
    n = int(input())
    natural_numbers = list(map(int, input().split()))
    if len(natural_numbers) > n or n < len(natural_numbers):
        return

    min_number = min(natural_numbers)
    counter = 0
    for deleter in range(min_number + 1).__reversed__():
        for number in natural_numbers:
            if number % deleter != 0:
                break
            else:
                counter += 1
        if counter == len(natural_numbers):
            return deleter
        counter = 0


print(meganode())
