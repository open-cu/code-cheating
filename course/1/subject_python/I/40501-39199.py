def cnt_even_digits_less_than(n: str, include_equal=True):
    even_digits = [str(i) for i in range(0, 10, 2)]
    cnt = 0
    for even_digit in even_digits:
        if include_equal and n == even_digit:
            cnt += 1
        if n > even_digit:
            cnt += 1
        elif n < even_digit:
            break

    return cnt


def true_even_cnt(n: str):
    if len(n) == 1:
        return cnt_even_digits_less_than(n)

    k = cnt_even_digits_less_than(n[0], include_equal=False)
    res = k * 5 ** (len(n) - 1)
    if int(n[0]) % 2 == 0:
        res += true_even_cnt(n[1:])
    return res


n = input()
print(true_even_cnt(n) - 1)
