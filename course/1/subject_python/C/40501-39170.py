def check_divisibility(first: int, second: int) -> int:
    first_res = first % second
    second_res = second % first

    result = first_res * second_res + 1
    return result


first, second = int(input()), int(input())
print(check_divisibility(first, second))
