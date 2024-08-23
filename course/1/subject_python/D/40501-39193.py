a = int(input())
b = int(input())

temp1 = (a // b) * b + (b // a) * a
temp2 = (a // b) + (b // a)


answer = a + b - temp1 // temp2

print(answer)
