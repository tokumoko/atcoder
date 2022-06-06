from collections import deque
n, m = map(int, input().split())
root = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    root[a].append(b)
    root[b].append(a)
q = int(input())
ans = [0] * q
for i in range(q):
    x, k = map(int, input().split())
    p = set()
    ans = 0
    que = deque()
    que.append((x, 0))
    while que:
        nxt, dist = que.popleft()
        if nxt in p:continue
        ans += nxt
        p.add(nxt)
        if dist == k:continue
        for j in root[nxt]:
            que.append((j, dist+1))
    print(ans)