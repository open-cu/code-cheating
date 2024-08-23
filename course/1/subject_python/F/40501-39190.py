import math

inputVal = int(input())

dividerCount = 0
for i in range(1, int(math.sqrt(inputVal) + 1)):
    if inputVal % i == 0:
        # The divisors take the form of either x * x or x * y
        if inputVal // i != i:
            dividerCount += 2
        else:
            dividerCount += 1

print(dividerCount)
