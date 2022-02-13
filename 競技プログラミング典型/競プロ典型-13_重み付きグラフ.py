#ダイクストラ法
import heapq
def DFS(s):
    dist=[10**15]*N
    que=[(0,s)]
    heapq.heapify(que)
    while len(que):
        t,n=heapq.heappop(que)
        if dist[n]>t:
            dist[n]=t
            for i,j in mati[n]:
                if dist[i]==10**15:
                    heapq.heappush(que,(dist[n]+j,i))
    return dist

N,M=map(int,input().split())
mati=[[] for _ in range(N)]
for i in range(M):
    A,B,C=map(int,input().split())
    A-=1;B-=1
    mati[A].append((B,C))
    mati[B].append((A,C))
ans1=DFS(0)
ans2=DFS(N-1)
for i in range(N):print(ans1[i]+ans2[i])