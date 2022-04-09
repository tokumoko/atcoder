from collections import deque
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = deque()
t = []
now = 10**10
for i in range(k-1, -1, -1):
    if now > a[i]:
        s.appendleft((a[i],i))
        now = a[i]
now = 0
for i in range(k,n):
    if now < a[i]:
        t.append((a[i], i))
        now = a[i]
i = 0
j = 0
ans = 10**10
while i < len(s) and j < len(t):
    if s[i][0] < t[j][0]:
        ans = min(ans, t[j][1]-s[i][1])
        i += 1
    else:
        j += 1
if ans != 10**10:
    print(ans)
else:
    print(-1)