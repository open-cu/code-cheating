def decode_str(s):
    res = []
    prev_digit = False
    digits = []

    for char in s:
        if char.isdigit():
            digits.append(char)
            prev_digit = True
        else:
            if prev_digit:
                repeats_cnt = int("".join(digits))
            else:
                repeats_cnt = 1

            res.append(char * repeats_cnt)
            digits = []
            prev_digit = False

    return "".join(res)


s = input()
print(decode_str(s))
