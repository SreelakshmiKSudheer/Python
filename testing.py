def Transpose(M):
    # Get the number of rows and columns in the input matrix M
    num_rows = len(M)
    num_cols = len(M[0]) if M else 0

    # Create an empty result matrix with swapped dimensions (columns x rows)
    transposed = [[0] * num_rows for _ in range(num_cols)]

    # Populate the transposed matrix
    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j][i] = M[i][j]

    return transposed

# Example usage:
# Suppose you have a matrix M, e.g., M = [[1, 2, 3], [4, 5, 6]]
# Call the function to calculate the transpose
# result = Transpose(M)
# Now, 'result' will contain the transposed matrix


n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)
print(Transpose(M))