N=int(input())
S=list(input())
dp=[0]*7
mod=10**9+7
for i in S:
    if i=='a':
        dp[0]+=1
        dp[0]%=mod
    elif i=='t':
        dp[1]+=dp[0]
        dp[1]%=mod
    elif i=='c':
        dp[2]+=dp[1]
        dp[2]%=mod
    elif i=='o':
        dp[3]+=dp[2]
        dp[3]%=mod
    elif i=='d':
        dp[4]+=dp[3]
        dp[4]%=mod
    elif i=='e':
        dp[5]+=dp[4]
        dp[5]%=mod
    elif i=='r':
        dp[6]+=dp[5]
        dp[6]%=mod
print(dp[6])