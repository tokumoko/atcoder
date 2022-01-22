import numpy as np
N,B,K=map(int,input().split())
c=list(map(int,input().split()))
A=np.array([[1]*B for _ in range(B)])
for i in range(B):A[i][i]=0
dp=np.array([[0]*B for _ in range(N)])
for i in c:dp[0][i%B]+=1
for i in range(N-1):
    dp[i+1]=np.dot(A,dp[i])
print(dp)