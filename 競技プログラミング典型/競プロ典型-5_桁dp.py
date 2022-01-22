N,B,K=map(int,input().split())
c=list(map(int,input().split()))
dp=[[0]*B for _ in range(N)]
mod=10**9+7
for j in c:
    dp[0][j%B]+=1
for i in range(N-1):
    for j in range(B):
        for k in c:
            a=(j*10+k)%B
            dp[i+1][a]+=dp[i][j]
            dp[i+1][a]%=mod
print(dp[N-1][0])