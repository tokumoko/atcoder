n = int(input())
z = [[0] * (1001) for _ in range(1001)]
for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    z[lx][ly] += 1
    z[lx][ry] -= 1
    z[rx][ly] -= 1
    z[rx][ry] += 1
ovlp = [0] * (n + 1)
for i in range(1001):
    for j in range(1001):
        if j != 0:
            z[i][j] += z[i][j-1]
    for j in range(1001):
        if i != 0:z[i][j] += z[i-1][j]
        ovlp[z[i][j]] += 1
for i in range(1,n+1):
    print(ovlp[i])