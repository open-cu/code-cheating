a = int(input())
b = int(input())
check = (a // b + 1) * (a // b) * (a % b) + (b // a + 1) * (b // a) * (b % a)
print(1 - check % 2 - check // 2)