from collections import deque


q = int(input())
t = deque()
for i in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        t.append((que[1], que[2]))
    else:
        c = que[1]
        ans = 0
        while c != 0:
            val = min(t[0][1], c)
            ans += t[0][0] * val
            c -= val
            k = t[0][1]
            if k == val:
                t.popleft()
            else:
                t[0] = (t[0][0], k-val)
        print(ans)