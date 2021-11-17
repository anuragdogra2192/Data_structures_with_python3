matrix = [[2,1,3],
          [6,5,4],
          [7,8,9]]
def minFallingPathSum(matrix):
    INF = 1000 * 1000
    row = len(matrix)
    col = len(matrix[0])
    dp = [[INF]*(col)]*(row-1)
    for i in range(row-1):
        for j in range(col):
            temp = matrix[i][j]                
            if(i != 0):
                temp = dp[i-1][j]
            dp[i][j] = min(dp[i][j], (temp + matrix[i+1][j]))
            if j >= 0 and j < col-1:
                dp[i][j+1] = min(dp[i][j+1], (temp + matrix[i+1][j+1]))
            if j <= col-1 and j > 0:
                dp[i][j-1] = min(dp[i][j-1], (temp + matrix[i+1][j-1]))
        if i<row-2:
            dp[i+1] = [INF]*(col)
    return (min(dp[-1]))

print(minFallingPathSum(matrix))

'''
Leet Code

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        INF = 100 * 100
        row = len(matrix)
        col = len(matrix[0])
        dp = [[INF]*(col)]*(row-1)
        
        if((len(matrix) * len(matrix[0])) == 1):
            return matrix[0][0]
        for i in range(row-1):
            for j in range(col):
                temp = matrix[i][j]                
                if(i != 0):
                    temp = dp[i-1][j]
                dp[i][j] = min(dp[i][j], (temp + matrix[i+1][j]))
                if j >= 0 and j < col-1:
                    dp[i][j+1] = min(dp[i][j+1], (temp + matrix[i+1][j+1]))
                if j <= col-1 and j > 0:
                    dp[i][j-1] = min(dp[i][j-1], (temp + matrix[i+1][j-1]))
            if i<row-2:
                dp[i+1] = [INF]*(col)
            
        return (min(dp[-1]))
'''