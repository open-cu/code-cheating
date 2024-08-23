def is_prime(number):
    start_number = 0
    iteration = 0

    if number % 2 != 0:
        start_number = 3
        iteration = 2
    else:
        start_number = 2
        iteration = 1

    while start_number * start_number <= number:
        if number % start_number == 0:
            return "composite"
        start_number += iteration
    return "prime"


print(is_prime(int(input())))
