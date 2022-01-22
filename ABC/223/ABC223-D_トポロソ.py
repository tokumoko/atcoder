import heapq
N,M=map(int,input().split())
ans=[]
G=[[]for _ in range(N+1)]
ind=[0]*(N)
que=[]
ans=[]
heapq.heapify(que)
for i in range(M):
    A,B=map(int,input().split())
    G[A].append(B)
    ind[B-1]+=1
for i in range(N):
    if ind[i]==0:
        que.append(i+1)
while len(que)!=0:
    a=heapq.heappop(que)
    for i in G[a]:
        ind[i-1]-=1
        if ind[i-1]==0:
            heapq.heappush(que,i)
    ans.append(a)
if len(ans)==N:
    for i in ans:print(i,end=' ')
else:print(-1)