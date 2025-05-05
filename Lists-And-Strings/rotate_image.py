matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]

# why n = 3 because n is the size of number of row and column
n = len(matrix)
for i in range(n // 2):
    for j in range(i, n - 1 - i):
        # save to top left
        topLeft = matrix[i][j]
        matrix[i][j] = matrix[n - 1 - j][i]
        matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 -j]
        matrix[n - 1 - i][n - 1 -j] = matrix[j][n - 1 -i]
        matrix[j][n - 1 -i] = topLeft

# Print rotate matrix
for row in matrix:
    print(row)
        
        
        
        
        
        
        
        # topRight = j, n - 1 - i
        # bottomRight =  n - 1 - i, n - 1 - j
        # bottomLeft = n - 1 - j, i
        # topLeft = i , j
        # print(j, n - 1 - i)
        # print(n - 1 - i, n - 1 - j)
        # print(n - 1 - j, i)
        # print(i, j)



        # print(f"Value at ({i},{j}) is {matrix[i][j]}")

        









#  matrix[0][0] → moves to → matrix[0][2]

# matrix[0][2] → moves to → matrix[2][2]

# matrix[2][2] → moves to → matrix[2][0]

# matrix[2][0] → moves to → matrix[0][0]       


# (i, j)           → (j, n - 1 - i)
# (j, n - 1 - i)   → (n - 1 - i, n - 1 - j)
# (n - 1 - i, n - 1 - j) → (n - 1 - j, i)
# (n - 1 - j, i)   → (i, j)
