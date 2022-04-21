from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
dist = [-1] * n
dist[0] = 0
que = deque()
que.append(0)
while que:
    x = que.popleft()
    for i in g[x]:
        if dist[i] != -1:continue
        que.append(i)
        dist[i] = dist[x] + 1
for i in dist:
    print(i)