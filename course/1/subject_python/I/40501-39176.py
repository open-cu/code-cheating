def solution(n: str) -> int:
    return sum(all(int(digit) % 2 == 0 for digit in str(i)) for i in range(1, int(n) + 1))


print(solution(input()))
