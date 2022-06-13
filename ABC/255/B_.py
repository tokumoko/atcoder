from math import sqrt
n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
s = []
t = []
for i in range(1, n+1):
    x, y = map(int, input().split())
    if i == a[cnt]:
        cnt = min(cnt+1, k-1)
        s.append((x, y))
    else:
        t.append((x, y))
ans = 0
for i, j in t:
    res = 10.0**9
    for k, l in s:
        res = min(res, sqrt((i-k)*(i-k) + (j-l)*(j-l)))
    ans = max(ans, res)
print(ans)