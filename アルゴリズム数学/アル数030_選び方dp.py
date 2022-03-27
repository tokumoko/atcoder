n, W = map(int, input().split())
dp = [0] * (W+1)
for i in range(n):
    w, v = map(int, input().split())
    for j in range(W-w, -1, -1):
        if dp[j] != 0:
            dp[j+w] = max(dp[j+w], dp[j] + v)
    dp[w] = v
print(max(dp))