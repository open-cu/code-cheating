n = int(input())
dividers = 0
for i in range(1, int(n**(1/2)) + 1):
    if n % i == 0:
        dividers += 1 
        if n / i != i:
            dividers += 1
print(dividers)