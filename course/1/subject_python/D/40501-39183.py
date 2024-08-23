def calc(first: int, second: int) -> int:
    num_1 = first//second
    num_2 = second//first
    return (first*num_1 + second*num_2)//(num_1 + num_2)


x, y = int(input()), int(input())
print(calc(x, y))
