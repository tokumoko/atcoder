from collections import deque
n, m = map(int, input().split())
glaph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a , b = a-1, b-1
    glaph[a].append(b)
    glaph[b].append(a)
t = [0] * n
flag = True
que = deque()
for k in range(n):
    if t[k] == 0:
        t[k] = 1
        que.append(k)
        while que:
            x = que.popleft()
            for i in glaph[x]:
                if t[i] == 0:
                    que.append(i)
                    if t[x] == 1:
                        t[i] = 2
                    else:
                        t[i] = 1
                elif t[i] == t[x]:
                    flag = False
print('Yes' if flag else 'No')