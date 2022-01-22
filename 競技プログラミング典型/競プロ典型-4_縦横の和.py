H,W=map(int,input().split())
A=[[]for _ in range(H)]
B=[0]*H
ans=[[0]*W for _ in range(H)]
for i in range(H):
    A[i]=list(map(int,input().split()))
    B[i]=sum(A[i])
for i in range(W):
    nsum=0
    for j in range(H):
        nsum+=A[j][i]
    for j in range(H):
        ans[j][i]=str(nsum+B[j]-A[j][i])
for i in range(H):print(' '.join(ans[i]))