n, m, k = map(int, input().split())
mod = 998244353
dp = [[0] * k for _ in range(n)]
for i in range(min(m, k)):
    dp[0][i] = 1
for i in range(1, n):
    for j in range(k):
        res = 0
        for l in range(max(0, j-m), j):
            res += dp[i-1][l]
        res %= mod
        dp[i][j] = res
print(sum(dp[n-1])%mod)