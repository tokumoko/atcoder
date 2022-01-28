N=int(input())
dp=[0]*5001
D=[0]*N;C=[0]*N;S=[0]*N
for i in range(N):
    D[i],C[i],S[i]=map(int,input().split())
zip_list=zip(D,C,S)
zip_sort=sorted(zip_list)
D,C,S=zip(*zip_sort)
for i in range(N):
    if D[i]<C[i]:continue
    for j in range(D[i]-C[i],-1,-1):
        dp[j+C[i]]=max(dp[j+C[i]],dp[j]+S[i])
print(max(dp))