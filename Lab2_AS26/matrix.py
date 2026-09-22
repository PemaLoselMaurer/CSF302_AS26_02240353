def smm(A, b):
    n = 2
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += A[i][k] * b[k][j]
    return c

def recursive_matrix_mul(A, B, i=0, j=0, result=None):
    if result is None:
        result = [[0 for _ in range(len(A))] for _ in range(len(A))]

    n = len(A)
    if i == n:
        return result

    if j == n:
        return recursive_matrix_mul(A, B, i + 1, 0, result)

    total = 0
    for k in range(n):
        total += A[i][k] * B[k][j]

    result[i][j] = total
    return recursive_matrix_mul(A, B, i, j + 1, result)

A = [[ 1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

c = smm(A, b)
print("Result of Square matrix:")
for row in c:
    print(row)  

d = recursive_matrix_mul(A, b)
print("Result of Recursive matrix multiplication:")
for row in d:
    print(row)  
