class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join([str(i) for i in el]) for el in self.matrix)

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return "Сложение матриц разной размерности не определено."
        else:
            result = []
            row = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                    if len(row) == len(self.matrix[0]):
                        result.append(row)
                        row = []
            result = Matrix(result)
            return result


m_1 = Matrix([[1, 2], [3, 4]])
print(m_1)

m_2 = Matrix([[2, 0], [1, -1]])
print(m_2)

print(m_1 + m_2)
