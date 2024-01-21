def primary_diagonal_sum(matrix):
    size = len(matrix)
    diagonal_sum = sum(matrix[i][i] for i in range(size))
    return diagonal_sum

n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


diagonal_sum = primary_diagonal_sum(matrix)

print(diagonal_sum)

