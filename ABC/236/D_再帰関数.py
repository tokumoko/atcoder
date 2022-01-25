def f(B,score):
    if len(B)==0:
        global ans
        ans=max(ans,score)
        return
    l=B[-1]
    for i in range(len(B)-1):
        c = B[i]
        f(B[:i]+B[i+1:-1] , score ^ A[c][l-c-1])

N=int(input())
A=[[] for _ in range(2*N-1)]
for i in range(2*N-1):A[i]=list(map(int,input().split()))
p=[i for i in range(2*N)]
ans=0
f(p,0)
print(ans)