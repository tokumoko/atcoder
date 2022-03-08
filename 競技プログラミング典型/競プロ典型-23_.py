from bisect import bisect_left


h,w=map(int,input().split())
c=[input() for _ in range(h)]
mod=10**9+7

no_con = [[] for _ in range(w+2)]


no_con[0] = [0]
no_con[1] = [0,1]
for i in range(w+1):
    if i + 1 <= w+1:
        for val in no_con[i]:
            no_con[i+1].append(val * 2)
    if i + 2 <= w+1:
        for val in no_con[i]:
            no_con[i+2].append(val * 4 + 1)
keys = []

for lower in range(w+1):
    upper = w+1-lower
    for u in no_con[upper]:
        for l in no_con[lower]:
            keys.append(l + (u << lower))
keys=sorted(set(keys))

nxt = []
for key in keys:
    zero = (key * 2) & ((1 << (w+1))-1)
    one = zero + 1
    nxt.append([
        bisect_left(keys, zero),
        bisect_left(keys, one),
    ])


dp=[[0] * len(keys) for _ in range(h*w)]
dp[0][0]=1
if c[0][0]=='.':
    dp[0][1]=1

for i in range(h):
    for j in range(w):
        if i == h-1 and j == w-1:continue
        now=i*w+j
        next=now+1
        for ind,state in enumerate(keys):
            val = dp[now][ind]
            zero, one = nxt[ind]
            dp[next][zero]+=val
            dp[next][zero]%=mod
            
            ni,nj = next // w , next % w
            left=state%2==0 or nj==0
            upleft=(state>>w)%2==0 or nj == 0
            up=(state>>(w-1))%2==0
            upright=(state>>(w-2))%2==0 or nj == w-1
            
            if left and upleft and up and upright and c[ni][nj]=='.':
                dp[next][one]+=val
                dp[next][one]%=mod
ans = 0
for i in dp[h*w-1]:
    ans += i
    ans%=mod
print(ans)