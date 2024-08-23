def solution(number_1: int, number_2: int) -> int:
    # 0 is not positive number!
    first_less = number_1 // number_2
    second_less = number_2 // number_1
    result = (first_less * number_1 + second_less * number_2) // (first_less + second_less)
    return result


num_1 = int(input())
num_2 = int(input())
print(solution(num_1, num_2))
