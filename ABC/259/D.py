from collections import deque
from math import sqrt
n = int(input())
sx, sy, tx, ty = map(int, input().split())
root = [[] for _ in range(n)]
cir = []
que = deque()
goal = [False] * n
for i in range(n):
    x, y, r = map(int, input().split())
    cir.append((x, y, r))
for i in range(n):
    x, y, r = cir[i]
    if sqrt((x-sx)*(x-sx) + (y-sy)*(y-sy)) == r:
        que.append(i)
    if sqrt((x-tx)*(x-tx) + (y-ty)*(y-ty)) == r:
        goal[i] = True
    for j in range(n):
        if i == j:continue
        nx, ny, nr = cir[j]
        dist = (x-nx)*(x-nx) + (y-ny)*(y-ny)
        if dist < (r-nr)*(r-nr) or dist > (r+nr)*(r+nr):
            continue
        root[i].append(j)
found = [True] * n
flag = False
while que:
    x = que.popleft()
    if found[x]:
        found[x] = False
    else:
        continue
    if goal[x]:
        flag = True
    for i in root[x]:
        if found[i]:
            que.append(i)
print('Yes' if flag else 'No')
