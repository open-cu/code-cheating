from typing import List


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def solution(numbers: List) -> int:
    if len(numbers) == 1:
        return numbers[0]
    nod = gcd(numbers[0], numbers[1])
    for number in numbers[2:]:
        nod = gcd(nod, number)
    return nod


input()
print(solution(list(map(int, input().split()))))
