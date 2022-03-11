from collections import deque
def BFS(w):
    dist=[0] * (n+1)
    dist[w]=1
    que.append(w)
    max_dist = 0
    max_index = 0
    while que:
        x=que.popleft()
        d = dist[x] + 1
        for i in t[x]:
            if dist[i]==0:
                que.append(i)
                dist[i]=d
                if max_dist < d:
                    max_dist = d
                    max_index = i
    return max_index,dist
n = int(input())
t = [[] for _ in range(n+1)]
que = []
que = deque()
for i in range(n-1):
    a, b = map(int,input().split())
    t[a].append(b)
    t[b].append(a)
ind,m = BFS(1)
o,dist = BFS(ind)
even = []
odd = []
for i in range(1, n+1):
    if dist[i] % 2 ==0:
        even.append(i)
    else:
        odd.append(i)
count = 0
if len(even) > len(odd):
    for i in range(n//2):
        print(even[i])
else:
    for i in range(n//2):
        print(odd[i])