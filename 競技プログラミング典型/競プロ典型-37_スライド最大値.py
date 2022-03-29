from collections import deque
w, n = map(int, input().split())
dp = [[-(10**18)] * (w + 1) for _ in range(n+1)]
dp[0][0] = 0
LRV = []
for i in range(n):
    LRV.append(tuple(map(int, input().split())))
for i in range(1,n+1):
    l, r, v = LRV[i-1]
    que = deque()
    nxt = 0
    for j in range(w+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j])
        low = j - r
        up = j - l
        while nxt <= up:
            val = dp[i-1][nxt]
            while len(que) > 0 and que[-1][0] <= val:
                que.pop()
            que.append((val, nxt))
            nxt += 1
        while len(que) > 0 and que[0][1] < low:
            que.popleft()
        if len(que) == 0:continue
        dp[i][j] = max(dp[i][j], que[0][0] + v)
if dp[n][w] < 0:
    print(-1)
else:
    print(dp[n][w])