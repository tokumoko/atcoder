q = int(input())
d = dict()
law = 10**9  + 1
high = 0
for i in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        if d.get(que[1], -1) == -1:
            d[que[1]] = 0
        d[que[1]] += 1
        if law > que[1]:
            law = que[1]
        if high < que[1]:
            high = que[1]
    if que[0] == 2 and d.get(que[1], -1) != -1:
        d[que[1]] -= que[2]
        if d[que[1]] < 1:
            d.pop(que[1])
            if que[1] == law:
                law = 10**9 + 1
                if len(d) != 0:
                    law = min(d)
            if que[1] == high:
                high = 0
                if len(d) != 0:
                    high = max(d)
    if que[0] == 3:
        print(high - law)