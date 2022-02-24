import numpy as np
N=int(input())
A=list(map(int,input().split()))
dp=np.array([[0]*1001 for _ in range(6)])
for i in range(N):
    for j in range(4,-1,-1):
        for k in range(1000-A[i]+1):
            if dp[j][k]!=0:
                dp[j+1][k+A[i]]+=dp[j][k]
    dp[1][A[i]]+=1
print(dp[5][1000])