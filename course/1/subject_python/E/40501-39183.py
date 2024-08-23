def calc(n: int) -> str:
    for x in range(2, int(n**(1/2))+1):
        print()
        if n % x == 0:
            return 'composite'
    return 'prime'


n = int(input())
print(calc(n))
