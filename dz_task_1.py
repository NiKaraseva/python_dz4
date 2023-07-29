# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


matrix = [[1, 2, 3], [4, 5, 6]]

def transpon_matrix(mat: list) -> list:
    zipped_mat = zip(*mat)
    return [list(row) for row in zipped_mat]

print(transpon_matrix(matrix))