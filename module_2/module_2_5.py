# Задача "Матрица воплоти"
def get_matrix(row, collumn, value):

    matrix = []

    for i in range(row):
        matrix.append([0] * collumn)

    for i in range(row):
        pass
        for j in range(collumn):
            matrix[i][j] = value

    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
