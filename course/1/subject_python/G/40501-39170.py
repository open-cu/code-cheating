def simple_multipliers(number: int) -> list:
    divider = 2
    div_list = []

    while divider * divider <= number:
        if number % divider == 0:
            div_list.append(divider)
            number = int(number / divider)
        else:
            divider += 1
    if number > 1:
        div_list.append(number)

    return div_list


n = int(input())
print(*simple_multipliers(n))
