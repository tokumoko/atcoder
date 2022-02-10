N=int(input())
A=list(map(int,input().split()))
dp=[0]*5
for i in range(N):
    n=A[i]//100
    if n==1:r=4
    elif n==2:r=3
    elif n==3:r=2
    else:r=1
    dp[0]+=dp[r]
    dp[n]+=1
print(dp[0])