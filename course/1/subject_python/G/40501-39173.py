n = int(input())
prime_divisor_list = []
while n % 2 == 0:
    prime_divisor_list.append(2)
    n //= 2
for i in range(3, int(n ** 0.5) + 1, 2):
    while n % i == 0:
        prime_divisor_list.append(i)
        n //= i
if n > 2:
    prime_divisor_list.append(n)
print(*prime_divisor_list)
