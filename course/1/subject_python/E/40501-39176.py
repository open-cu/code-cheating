def solution(number: int):
    for i in range(2, round(number ** 0.5) + 1):
        if number % i == 0:
            return 'composite'
    return 'prime'


print(solution(int(input())))
