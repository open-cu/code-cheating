num1 = int(input())
num2 = int(input())
if num2 != 0 and (num1 % num2 == 0 or num2 % num1 == 0):
    print(1)
else:
    print(7)
