N,S=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
flag=[False]*(S+1)
flag[0]=True
if A[0]<=S:flag[A[0]]=True
for i in range(1,N):
    if A[i]>S:continue
    for j in range(S-A[i],-1,-1):
        if flag[j]:flag[j+A[i]]=True
print('Yes' if flag[S] else 'No')