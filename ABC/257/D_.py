import heapq
from math import ceil
n = int(input())
dist = [[0] * n for _ in range(n)]
city = []
inf = 10**9 + 1
for i in range(n):
    x, y, p = map(int, input().split())
    city.append((x, y, p))
for i in range(n):
    x, y, p = city[i]
    for j in range(n):
        if i == j:
            dist[i][j] = inf
            continue
        nx, ny, np = city[j]
        dist[i][j] = ceil((abs(x-nx)+abs(y-ny)) / p)
st = 1
ed = 4 * 10**9
while True:
    x = (st + ed) // 2
    for i in range(n):
        