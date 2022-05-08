n, q = map(int, input().split())
ball = [i for i in range(1, n+1)]
ball_ind = dict()
for i in range(1, n+1):
    ball_ind[i] = i-1
for i in range(q):
    x = int(input())
    s = ball_ind[x]
    if s == n-1:
        t = s-1
    else:
        t = s+1
    ball_ind[ball[s]] = t
    ball_ind[ball[t]] = s
    ball[s], ball[t] = ball[t], ball[s]
print(*ball)