n, w = map(int, input().split())
a = list(map(int, input().split()))
inf = 10**18
home = [list(map(int, input().split())) for _ in range(n)]
s, t = n, n+1
edge = [[0] * (n+2) for _ in range(n+2)]
for i in range(n):
    for j in home[i][1:]:
        edge[i][j-1] = inf
    edge[s][i] = w
    edge[i][t] = a[i]
pos = [False] * (n+2)
def dfs(s, t, f):
    pos[s] = True
    if s == t:return f
    for to in range(n+2):
        if pos[to]:continue
        if edge[s][to] == 0:continue
        tmp = dfs(to, t, min(f, edge[s][to]))
        if tmp > 0:
            edge[s][to] -= tmp
            edge[to][s] += tmp
            return tmp
    return 0
def max_flow(s, t):
    global pos
    ans = 0
    while True:
        pos = [False] * (n+2)
        f = dfs(s, t, inf)
        if f == 0:return ans
        ans += f
print(sum(a) - max_flow(s, t))