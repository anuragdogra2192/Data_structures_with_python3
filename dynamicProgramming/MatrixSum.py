X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0]*len(X[0])]*len(X)
t = 0
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = result[i][j] + Y[i][j]
       if i<len(X)-1:
           result[i+1] = [0]*len(X[0])
print(result)