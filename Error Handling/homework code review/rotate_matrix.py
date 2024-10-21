class MatrixContentError(Exception):
    pass


class MatrixSizeError(Exception):
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    if not all(len(row) == matrix_length for row in matrix):
        raise MatrixSizeError("The size of the matrix is not a perfect square")

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()


matrix_list = []

while True:
    line = input().split()
    if not line:
        break
    for i in line:
        if i.isalpha():
            raise MatrixContentError("The matrix must consist of only integers")
    matrix_list.append([int(i) for i in line])

rotate_matrix(matrix_list)

for row in matrix_list:
    print(*row, sep=' ')
