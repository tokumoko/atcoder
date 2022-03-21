n, m, k, s, t, x = map(int, input().split())
mod = 998244353
z = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    z[u].append(v)
    z[v].append(u)
