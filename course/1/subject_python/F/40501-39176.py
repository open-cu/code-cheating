def solution(n: int) -> int:
    if n == 1:
        return 1
    counter = 0
    for i in range(1, int(n ** 0.5)):
        counter += n % i == 0
    return counter * 2 + int(int(n ** 0.5) ** 2 == n)


print(solution(int(input())))
