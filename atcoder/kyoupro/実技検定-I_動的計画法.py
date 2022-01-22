n,m = map(int,input().split())
dp = [10**12]*(1<<n)
dp[0] = 0
for i in range(m):
    s,c = list(input().split())
    c = int(c)
    now = 0
    for j in range(n):#YYY => 111,   YNY => 101 などに変換
        now <<= 1
        if s[j] == 'Y':
            now += 1
    for j in range(1<<n):#ここらへんが動的計画法
        dp[j|now] = min(dp[j|now],dp[j]+c)
    print(dp)
print(-1 if dp[-1] == 10**12 else dp[-1])