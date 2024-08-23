n = int(input())
init_number = 0
resulting_number = 1
for i in range(n - 1):
    aux_number = init_number + resulting_number
    init_number, resulting_number = resulting_number, aux_number

print(resulting_number)