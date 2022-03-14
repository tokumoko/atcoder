n, m = map(int, input().split())
g = []
dp = [[10**10] * n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1;b -= 1
    g.append((a,b,c))
    dp[a][b] = c
    dp[b][a] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
ans = 0
for a,b,c in g:
    flag = False
    for i in range(n):
        if i == a or i == b:continue
        if dp[a][i] + dp[i][b] <= c:
            flag = True
    if flag:ans += 1
print(ans)