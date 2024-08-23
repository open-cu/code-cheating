_ = input()


def check_if_possible(array):
    if len(array) == 0:
        return True, []
    if array[0] > -array[0]:
        array[0] = -array[0]

    for i in range(1, len(array)):
        if array[i] >= array[i - 1]:
            if -array[i] >= array[i - 1] and -array[i] < array[i]:
                array[i] = -array[i]
        else:
            if -array[i] >= array[i - 1]:
                array[i] = -array[i]
            else:
                return False, []
    return True, array


array = list(map(int, input().split()))

flag, array = check_if_possible(array)
if flag:
    print("Yes")
    print(*array)
else:
    print("No")
