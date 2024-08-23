def euclidean_algorithm(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


if __name__ == '__main__':
    numbers_count = int(input())
    numbers = [int(element) for element in input().split()]
    if numbers_count == 1:
        print(numbers[0])
    else:
        prev = numbers[0]
        for i in range(1, numbers_count):
            prev = euclidean_algorithm(prev, numbers[i])

        print(prev)
