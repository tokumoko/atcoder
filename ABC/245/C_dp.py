n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[False] * 2 for _ in range(n)]
dp[0][0] = dp[0][1] = True
for i in range(n-1):
    if dp[i][0]:
        if abs(a[i+1] - a[i]) <= k: dp[i+1][0] = True
        if abs(b[i+1] - a[i]) <= k: dp[i+1][1] = True
    if dp[i][1]:
        if abs(a[i+1] - b[i]) <= k: dp[i+1][0] = True
        if abs(b[i+1] - b[i]) <= k: dp[i+1][1] = True
if dp[n-1][0] or dp[n-1][1]:
    print('Yes')
else:
    print('No')