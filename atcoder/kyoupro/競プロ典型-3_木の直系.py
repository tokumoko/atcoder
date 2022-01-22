def BFS(w):
    dist=[0]*N
    dist[w]=1
    que.append(w)
    while que:
        x=que.pop(0)
        for i in tosi[x]:
            if dist[i]==0:
                que.append(i)
                dist[i]=dist[x]+1
    return max(dist),dist.index(max(dist))

N=int(input())
tosi=[[]for _ in range(N)]
que=[]
for i in range(N-1):
    A,B=map(int,input().split())
    A-=1
    B-=1
    tosi[A].append(B)
    tosi[B].append(A)
y,z=BFS(0)
ans,y=BFS(z)
print(ans)