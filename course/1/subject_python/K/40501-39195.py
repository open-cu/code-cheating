def unrle(s: str):
    num = ""

    for c in s:
        if c.isnumeric():
            num += c
        else:
            to_print = c * (1 if num == "" else int(num))
            print(to_print, end="")
            num = ""


def solution():
    s = input()
    unrle(s)


solution()
