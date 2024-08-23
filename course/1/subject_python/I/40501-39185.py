def is_truly_even(num: int) -> bool:
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True


def count_truly_even_nums(n):
    cnt = 0
    for num in range(2, n+1, 2):
        if is_truly_even(num):
            cnt += 1
    return cnt


def main():
    n = int(input())
    print(count_truly_even_nums(n))
    

if __name__ == "__main__":
    main()