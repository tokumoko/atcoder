from collections import deque
n, m = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
field = [list(input()) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
inf = 10**6
for i in range(n):
    for j in range(m):
        if field[i][j] == '#':
            dist[i][j] = inf
que = deque()
que.append((sx-1, sy-1))
dist[sx-1][sy-1] = 0
while que:
    x, y = que.popleft()
    k = dist[x][y]
    if dist[x-1][y] == -1:
        que.append((x-1, y))
        dist[x-1][y] = k+1
    if dist[x+1][y] == -1:
        que.append((x+1, y))
        dist[x+1][y] = k+1
    if dist[x][y-1] == -1:
        que.append((x, y-1))
        dist[x][y-1] = k+1
    if dist[x][y+1] == -1:
        que.append((x, y+1))
        dist[x][y+1] = k+1
print(dist[gx-1][gy-1])