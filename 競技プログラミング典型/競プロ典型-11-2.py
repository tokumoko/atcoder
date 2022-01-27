from collections import defaultdict
N=int(input())
dp=[defaultdict(list) for _ in range(N)]
D=[0]*N;C=[0]*N;S=[0]*N
for i in range(N):
    D[i],C[i],S[i]=map(int,input().split())
zip_list=zip(D,C,S)
zip_sort=sorted(zip_list)
D,C,S=zip(*zip_sort)
if C[0]>D[0]:dp[0][0]=0
else:dp[0][C[0]]=S[0]