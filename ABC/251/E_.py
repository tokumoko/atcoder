n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[0] = a[0]
dp[1] = a[0] + a[1]
for i in range(2, n):
    dp[i] = min(dp[i-2], dp[i-1]) + a[i]
ans = min(dp[n-1], dp[n-2])
dp = [0] * n
dp[0] = 0
dp[1] = a[1]
for i in range(2, n):
    dp[i] = min(dp[i-2], dp[i-1]) + a[i]
if len(a) > 3 and a[1] < a[2]:
    ans = min(ans, dp[n-2])
print(min(ans, dp[n-1]))