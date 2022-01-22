import itertools
N,M=map(int,input().split())
S=[""]*M
C=[0]*M
ans=10**100
for i in range(M):
    list=input()
    S[i]=list[:N]
    C[i]=int(list[N+1:])
for p in itertools.product([0,1],repeat=M):
    flag=[False]*N
    kingaku=0
    for i in range(M):
        if p[i]==1:
            for j in range(N):
                if S[i][j]=='Y':
                    flag[j]=True
    if False not in flag:
        for i in range(M):
            if p[i]==1:
                kingaku+=C[i]
        ans=min(ans,kingaku)
if ans==10**100:ans=-1
print(ans)