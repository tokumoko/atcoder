import heapq
n, m = map(int, input().split())
root = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    root[a].append((c, b, i+1))
    root[b].append((c, a, i+1))
que = []
heapq.heapify(que)
for time, to, num in root[0]:
    heapq.heappush(que, (time, to, num))
dist = [-1] * n
dist[0] = 0
ans = []
for i in range(n-1):
    while True:
        time, frm, num = heapq.heappop(que)
        if dist[frm] == -1:break
    ans.append(num)
    dist[frm] = time
    for time, to, num in root[frm]:
        if dist[to] != -1:continue
        heapq.heappush(que, (time+dist[frm], to, num))
print(*ans)