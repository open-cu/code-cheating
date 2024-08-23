from typing import List


def solution(sequence: List) -> List:
    last = sequence[0]
    result = []
    for i in range(1, len(sequence)):
        if last >= sequence[i]:
            result.append(last)
        last = sequence[i]
    result.append(last)
    return result


input()
seq = list(map(int, input().split()))
result = solution(seq)
print(len(result))
print(* result)
