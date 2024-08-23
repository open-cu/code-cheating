n_1 = int(input())
n_2 = int(input())


def check_partibility(n_1, n_2):
    if n_1 % n_2 == 0 or n_2 % n_1 == 0:
        return 1
    else:
        return 2


print(check_partibility(n_1, n_2))
