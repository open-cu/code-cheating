import math


def get_prime_divisors(value: int) -> list[int]:
    dividers = []
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            while value % i == 0:
                dividers.append(i)
                value //= i

        if value == 1:
            return dividers
    if value != 1:
        dividers.append(value)

    return dividers


if __name__ == '__main__':
    input_val = int(input())
    print(*get_prime_divisors(input_val))
