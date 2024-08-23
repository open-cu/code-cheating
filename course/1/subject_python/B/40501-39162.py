def fibonacci(n_number_fib):
    first_number = 1
    second_number = 1

    if n_number_fib == 1:
        return first_number

    if n_number_fib == 2:
        return second_number

    for _ in range(n_number_fib - 2):
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number

    return second_number


print(fibonacci(int(input())))
