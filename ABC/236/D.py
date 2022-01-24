N=int(input())
A=[[] for _ in range(2*N-1)]
for i in range(2*N-1):A[i]=list(map(int,input().split()))
p=[i for i in range(1,2*N)]
for i in range(2*N-1):
    k=p.pop(i)