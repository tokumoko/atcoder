import collections
N,Q=map(int,input().split())
a=list(map(int,input().split()))
m=collections.defaultdict(list)
for i in range(N):m[a[i]].append(i+1)
for i in range(Q):
    x,k=map(int,input().split())
    print(m[x][k-1] if k<=len(m[x]) else '-1')