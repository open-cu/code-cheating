def check_str(two_symbols: str) -> str:
    count = 0
    for _ in range(len(two_symbols)):
        if ord('9') >= ord(two_symbols[_]) >= ord('0'):
            count += 1

    if count == 1:
        return 'YES'
    return 'NO'


string = input()
if 1 < len(string) < 3:
    print(check_str(string))
