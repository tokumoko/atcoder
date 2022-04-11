k = int(input())
mod = 10**9 + 7
if k % 9 != 0:
    print(0)
    exit()
dp = [0] * k
for i in range(9):
    dp[i] = 1
for i in range(k):
    for j in range(i-9,i):
        if j < 0:continue
        dp[i] += dp[j]
    dp[i] %= mod
print(dp[k-1])