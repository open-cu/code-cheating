from typing import List


def solution(array: List) -> None:
    array[0] = min(array[0], - array[0])
    for i in range(1, len(array)):
        possible_min = min(array[i], - array[i])
        if array[i - 1] <= possible_min:
            array[i] = possible_min
            continue
        elif array[i - 1] <= - possible_min:
            array[i] = - possible_min
            continue
        else:
            print('No')
            return
    print('Yes')
    print(*array)


input()
arr = list(map(int, input().split()))
solution(arr)
