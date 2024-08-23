def solution(n: int) -> int:
    number_1 = number_2 = 1
    for _ in range(2, n):
        number_1, number_2 = number_2, number_1 + number_2
    return number_2


print(solution(int(input())))
