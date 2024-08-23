a = int(input(''))
b = int(input(''))

# скобка (((a // b) * a) + ((b // a) * b)) даёт a + b, если a = b, и min(a,b)*q, где max(a,b) = min(a,b)*q + r иначе
# скобка ((a // b) + (b // a))) даёт 2, если a = b, и max(a,b) // min(a,b) иначе
print((((a // b) * a) + ((b // a) * b)) // ((a // b) + (b // a)))
