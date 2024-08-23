n = int(input())
prime_flg = True
if n == 1:
    prime_flg = False
elif n == 2:
    pass
elif n % 2 == 0:
    prime_flg = False
else:
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            prime_flg = False
            break
print('prime' if prime_flg else 'composite')