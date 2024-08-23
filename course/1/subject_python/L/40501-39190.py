def non_decreasing_list():
    elements_count = int(input())
    elements = [int(element) for element in input().split()]

    if elements[0] > 0:
        elements[0] = -elements[0]

    if len(elements) == 1:
        print(f'Yes\n{elements[0]}')
        return

    for i in range(1, elements_count):
        if elements[i] > elements[i - 1] and elements[i] > 0 and -elements[i] >= elements[i - 1]:
            elements[i] = -elements[i]
        elif elements[i] < elements[i - 1]:
            if -elements[i] >= elements[i - 1]:
                elements[i] = -elements[i]
            else:
                print('No')
                return

    print('Yes')
    print(*elements)


if __name__ == '__main__':
    non_decreasing_list()
