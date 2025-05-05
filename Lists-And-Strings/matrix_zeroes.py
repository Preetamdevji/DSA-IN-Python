# You’re given a 2D matrix. If an element is 0, set its entire row and column to 0.

matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [0, 1, 1]
]

# find the index where zero is present in row and column

zeroRows = set()
zeroCols = set()


for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == 0:
            print(f"Zero found at Row {i}, Column {j}")
            zeroRows.add(i)
            zeroCols.add(j)
            print(zeroRows,zeroCols)
            

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i in zeroRows or j in zeroCols:
            matrix[i][j] = 0

print(matrix)