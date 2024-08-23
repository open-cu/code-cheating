n = int(input())
div_to_quantity = dict()

for divider in range(2, int(n ** (1 / 2)) + 1):
    while n % divider == 0:
        div_to_quantity[divider] = div_to_quantity.get(divider, 0) + 1
        n //= divider
if n != 1:
    div_to_quantity[n] = div_to_quantity.get(n, 0) + 1

for divider, quantity in sorted(div_to_quantity.items()):
    for i in range(quantity):
        print(divider, end=' ')
