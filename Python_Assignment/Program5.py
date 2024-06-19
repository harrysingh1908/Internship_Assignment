def matrix_multiply(matrix1, matrix2):
    
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in first matrix must be equal to the number of rows in the second matrix.")

    # Initialize the resultant matrix with zeros
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Example usage:
matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

result = matrix_multiply(matrix1, matrix2)
print("Resultant Matrix:")
for row in result:
    print(row)
