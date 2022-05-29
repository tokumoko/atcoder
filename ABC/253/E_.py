n, m, k = map(int, input().split())
dp = [[0] * (m) for _ in range(n)]
mod = 998244353
if k == 0:
    print(pow(m, n, mod))
    exit()
for i in range(m):
    dp[0][i] = 1
for i in range(1, n):
    p = sum(dp[i-1][k:])
    for j in range(1, m+1):
        p %= mod
        dp[i][j-1] = p
        if j+k-1 < m:
            p -= dp[i-1][j+k-1]
        if j-k >= 0:
            p += dp[i-1][j-k]
print(sum(dp[n-1]) % mod)