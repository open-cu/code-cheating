def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())

arr = list(map(int, input().split()))
if (n == 1):
    print(arr[0])
else:
    ans = gcd(arr[0], arr[1])
    for i in range(2, n):
        ans = gcd(ans, arr[i])
    print(ans)
