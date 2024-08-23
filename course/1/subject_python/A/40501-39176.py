def solution(s: str) -> str:
    if s[0].isdigit() and s[1].isalpha():
        return 'YES'
    elif s[1].isdigit() and s[0].isalpha():
        return 'YES'
    return 'NO'


s = input()
print(solution(s))
