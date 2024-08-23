def matmul(A, B):
    # A.shape = (m, k); B.shape = (k, n)
    m = len(A)
    k = len(A[0])
    n = len(B[0])
    C = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for t in range(k):
                C[i][j] += A[i][t] * B[t][j]

    return C


def matrix_power(A, n):
    if n < 0:
        return None
    if n == 0:
        return [[1, 0], [0, 1]]

    A_half_power = matrix_power(A, n // 2)
    if n % 2 == 0:
        return matmul(A_half_power, A_half_power)
    else:
        return matmul(A, matmul(A_half_power, A_half_power))


# O(logn)
A = [[1, 1], [1, 0]]
n = int(input())
f_n = matrix_power(A, n)[0][1]
print(f_n)
