def calc(s: list) -> list:
    result = []
    num = []
    for x in range(len(s)):
        if s[x].isnumeric():
            num.append(s[x])
        else:
            if not num:
                num = ['1']
            num = ''.join(s[x] * int(''.join(num)))
            result.append(num)
            num = []
    return result


string = list(input())
print(''.join(calc(string)))
