def devisors_cnt(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 2

    if int(n ** 0.5) ** 2 == n:
        cnt -= 1
    return cnt


def main():
    n = int(input())
    print(devisors_cnt(n))
    

if __name__ == "__main__":
    main()