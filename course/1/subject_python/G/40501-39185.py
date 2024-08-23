def factorization(num):
    res_nums = []

    i = 2

    while i*i <= num:
        if num % i == 0:
            res_nums.append(i)
            num /= i
        else:
            i += 1
    if num != 1:
        res_nums.append(int(num))
    return res_nums


def main():
    n = int(input())
    print(*factorization(n))
    

if __name__ == "__main__":
    main()