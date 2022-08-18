n, m = map(int, input().split())
x = [0] + list(map(int, input().split()))
ans = 0
dp = [[0] * (n+1) for _ in range(n+1)]
bonus = [0] * (n + 1)
for _ in range(m):
    c, y = map(int, input().split())
    bonus[c] = y
for i in range(1, n+1):
    large = 0
    for j in range(i, -1, -1):
        if j == 0:
            dp[i][j] = large
        else:
            large = max(large, dp[i-1][j-1])
            dp[i][j] = dp[i-1][j-1] + x[i] + bonus[j]
print(max(dp[n]))