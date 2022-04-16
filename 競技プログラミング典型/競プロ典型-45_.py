n, k = map(int, input().split())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())
dist = []
for i in range(n-1):
    for j in range(i+1, n):
        val = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        dist.append((val, i, j))
print(sorted(dist,reverse=True))
for i, j, k