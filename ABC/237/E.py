N,M=map(int,input().split())
H=list(map(int,input().split()))
bridge=[[] for _ in range(N)]
for i in range(M):
    U,V=map(int,input().split())
    U-=1
    V-=1
    bridge[U].append(V)
    bridge[V].append(U)
