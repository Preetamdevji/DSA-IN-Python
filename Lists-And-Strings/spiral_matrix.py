n = 3        # 3 X 3

# under the hood list comprehension do this 
# matrix = []
# for i in range(n):
#      row = []
#      for j in range(n):
#           row.append(0)
#      matrix.append(row)

# print(matrix)
     
# In a list comprehension, the syntax must follow this structure:
# [<expression> for <variable> in <iterable>]

matrix = [[0 for index in range(n)] for index in range(n)]         #nested list comprehension
print(matrix)


top = 0
bottom = n - 1
left = 0
right = n - 1

number = 1

while top <= bottom and left <= right:
     # Move left to right
     for j in range(left, right + 1):        # range function is exclusive it does not take the last value, therefore we use right + 1, right now its work like inclusive
          print("j", j)
          print("matrix", matrix[top][j])
          matrix[top][j] = number
          number += 1
     top += 1

     for i in range(top, bottom + 1):
          matrix[i][right] = number
          number += 1
     right -= 1

     if top <= bottom:
          for j in range(right, left - 1, -1):
               matrix[bottom][j] = number
               number += 1
          bottom -= 1

     if left <= right:
          for i in range(bottom, top - 1, - 1):
               matrix[i][left] = number
               number += 1
          left += 1


for row in matrix:
     print(row)