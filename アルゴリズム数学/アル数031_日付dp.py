n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[0] = a[0]
dp[1] = a[1]
for i in range(2,n):
    dp[i] = max(dp[i-2], dp[i-3]) + a[i]
print(max(dp[n-1], dp[n-2]))