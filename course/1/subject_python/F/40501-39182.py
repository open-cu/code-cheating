number = int(input())
counter = 0
for i in range(1, int(number**0.5) + 1):
    if number % i == 0:
        counter += 2
if number**0.5 == int(number**0.5):
    counter -= 1
print(counter)