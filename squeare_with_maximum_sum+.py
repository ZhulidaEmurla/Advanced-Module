def find_max_submatrix(matrix):
    max_sum = float('-inf')
    max_submatrix = None

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
            if current_sum > max_sum:
                max_sum = current_sum
                max_submatrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]

    return max_submatrix, max_sum

rows, columns = map(int, input().split(', '))

matrix = []
for _ in range(rows):
    row = list(map(int, input().split(', ')))
    matrix.append(row)

max_submatrix, max_sum = find_max_submatrix(matrix)

print('\n'.join([' '.join(map(str, row)) for row in max_submatrix]))
print(max_sum)
