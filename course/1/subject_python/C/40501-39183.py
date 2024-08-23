def calc(first: int, second: int) -> int:
    number = (first % second + first - 1)//first +\
             (second % first + second - 1)//second
    return number//2 + 1


x, y = int(input()), int(input())
print(calc(x, y))
