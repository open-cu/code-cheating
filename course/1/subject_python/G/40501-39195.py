def get_divs(n: int):
    res = []
    
    while n % 2 == 0:
        res.append(2)
        n //= 2
        
    d = 3
    while d * d <= n:
        while n % d == 0:
            res.append(d)
            n //= d
        d += 2
    
    if n > 1:
        res.append(n)
    return res


def solution():
    n = int(input())
    print(*get_divs(n))


solution()