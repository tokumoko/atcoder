from math import sqrt
n = int(input())
sx, sy, tx, ty = map(int, input().split())
root = [[] for _ in range(n)]
cir = []
for i in range(n):
    x, y, r = map(int, input().split())
    cir.append((x, y, r))
for i in range(n-1):
    x, y, r = cir[i]
    for j in range(i+1, n):
        nx, ny, _ = cir[j]
        if sqrt((x-nx)*(x-nx) + (y-ny)*(y-ny)) == r:
            