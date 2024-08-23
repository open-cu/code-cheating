n = int(input())
divisors = {1, n}
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        divisors.add(i)
        divisors.add(n // i)
print(len(divisors))