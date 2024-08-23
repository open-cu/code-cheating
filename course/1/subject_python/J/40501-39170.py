def mega_nod(n: int, numbers: list) -> int:
    if len(numbers) == 1:
        return numbers[0]
    else:
        for i in range(n - 1):
            if numbers[i] > numbers[i + 1]:
                rest_1 = numbers[i + 1]
                rest_2 = numbers[i] % numbers[i + 1]
                while rest_2 != 0:
                    rest_1, rest_2 = rest_2, rest_1 % rest_2
            else:
                rest_1 = numbers[i]
                rest_2 = numbers[i + 1] % numbers[i]
                while rest_2 != 0:
                    rest_1, rest_2 = rest_2, rest_1 % rest_2
            numbers[i + 1] = rest_1
    return numbers[-1]


n_test = int(input())
numbers_test = [int(i) for i in input().split(" ")]
print(mega_nod(n_test, numbers_test))
