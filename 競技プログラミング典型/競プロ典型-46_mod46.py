n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
mod = 46
dp = [[0] * 46 for _ in range(3)]
mod_abc = [[0] * 46 for _ in range(3)]
for i in range(n):
    mod_abc[0][a[i]%mod] += 1
    mod_abc[1][b[i]%mod] += 1
    mod_abc[2][c[i]%mod] += 1
for i in range(46):
    dp[0][i] = mod_abc[0][i]
for k in range(2):
    for i in range(46):
        for j in range(46):
            ind = (i+j) % mod
            dp[k+1][ind] += dp[k][i] * mod_abc[k+1][j]
print(dp[2][0])