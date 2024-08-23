def solution(number_1: int, number_2: int) -> int:
    return (number_1 % number_2) * (number_2 % number_1) + 1


num_1 = int(input())
num_2 = int(input())
print(int(solution(num_1, num_2)))
