X = [[1,3,2],
    [3 ,6,8],
    [5 ,2,1]]
# 3x3 matrix
Y = [[6,8,6],
    [6,3,3],
    [2,5,1]]
# result is 3x4
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
for r in result:
   print(r)
