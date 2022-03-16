import numpy as np
n = int(input())
z = np.array([[0] * (5) for _ in range(5)])
for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    lx -= 1;ly -= 1;rx -= 1;ry -= 1
    z[lx][ly] += 1
    z[lx][ry] -= 1
    z[rx][ly] -= 1
    z[rx][ry] += 1
ovlp = [0] * (n + 1)
for i in range(5):
    for j in range(5):
        if j != 0:
            z[i][j] += z[i][j-1]
    for j in range(5):
        if i != 0:z[i][j] += z[i-1][j]
        ovlp[z[i][j]] += 1
print(z)
print(ovlp)