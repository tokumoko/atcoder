N,S=map(int,input().split())
A=list(map(int,input().split()))
dp=[[0]*(S+1) for _ in range(N)]
dp[0][0]=1
if A[0]<=S:dp[0][A[0]]=1
for i in range(1,N):
    for j in range(S+1):
        dp[i][j]+=dp[i-1][j]
        if A[i]+j<=S:dp[i][j+A[i]]+=dp[i-1][j]
print('No' if dp[N-1][S]==0 else 'Yes')