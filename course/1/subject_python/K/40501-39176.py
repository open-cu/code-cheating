def solution(s: str) -> str:
    result = []
    last_symbol = ''
    for i in range(len(s)):

        if s[i].isalpha() and last_symbol.isdigit():
            result.append(int(last_symbol) * s[i])
        elif s[i].isalpha():
            result.append(s[i])

        if last_symbol.isdigit():
            last_symbol += s[i]
        else:
            last_symbol = s[i]

    return "".join(result)


s = input()
print(solution(s))

