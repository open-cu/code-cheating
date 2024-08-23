def check_simple(number: int) -> str:
    if number == 2:
        return 'prime'
    elif number % 2 != 0:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return 'composite'
                break
        else:
            return 'prime'
    else:
        return 'composite'


number = int(input())
print(check_simple(number))
