n=int(input())
a=list(map(int,input().split()))
dp=[[10**18]*(2*n+1) for _ in range(2*n+1)]
for i in range(2*n+1):
    dp[i][i]=0
for w in range(2,2*n+1,2):
    for l in range(2*n):
        r=w+l
        if r>2*n:break
        for mid in range(l+2,r,2):
            dp[l][r]=min(dp[l][r],dp[l][mid]+dp[mid][r])
        dp[l][r]=min(dp[l][r],dp[l+1][r-1]+abs(a[l]-a[r-1]))
print(dp[0][2*n])