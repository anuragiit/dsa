import sys
def matrixMultiplication(N, arr):
        dp=[[0 for i in range(N)] for i in range(N)]
        if N>2:
            for L in range(3,N+1):
                for i in range(N-L+1):
                    j=i+L-1
                    mini=sys.maxsize
                    for k in range(i+1,j):
                        if mini>dp[i][k]+dp[k][j]+arr[i]*arr[k]*arr[j]:
                            mini=dp[i][k]+dp[k][j]+arr[i]*arr[k]*arr[j]
                    dp[i][j]=mini
        return dp[0][N-1]

arr=[10,30,5,60]
print(matrixMultiplication(len(arr),arr))
