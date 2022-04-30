from collections import deque


n, m = map(int, input().split())
t = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    t[a].append(b)
    t[b].append(a)
que = deque()
dist = [-1] * n
flag = True
for i in range(n):
    if dist[i] == 0 or dist[i] == 1:
        continue
    que.append(i)
    while que:
        x = que.popleft()
        k = dist[x]
        for i in t[x]:
            if dist[i] == -1:
                que.append(i)
                if k == 0:
                    dist[i] = 1
                else:
                    dist[i] = 0
            elif dist[i] == k:
                flag = False
print('Yes' if flag else 'No')