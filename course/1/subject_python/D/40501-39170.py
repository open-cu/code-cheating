def find_max(first: int, second: int) -> int:
    res_1 = first // second
    res_2 = second // first
    result = (res_1 * first + res_2 * second) // (res_1 + res_2)
    return result


test_1, test_2 = int(input()), int(input())
print(find_max(test_1, test_2))
