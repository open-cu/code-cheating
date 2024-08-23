import math

primeCandidate = int(input())
isPrime = True

for i in range(2, int(math.sqrt(primeCandidate)) + 1):
    if primeCandidate % i == 0:
        isPrime = False
        break

print('prime' if isPrime else 'composite')
