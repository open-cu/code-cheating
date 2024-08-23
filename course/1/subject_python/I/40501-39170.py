def truly_even_numbers(number: int) -> int:
    counter = 0
    for i in range(1, number + 1):
        digits = str(i)
        flag = True
        for digit in digits:
            if int(digit) % 2 != 0:
                flag = False
                break
        if flag:
            counter += 1
    return counter


test = int(input())
print(truly_even_numbers(test))
