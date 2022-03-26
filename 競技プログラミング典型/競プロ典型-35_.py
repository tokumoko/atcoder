import sys
sys.setrecursionlimit(200000)
def bfs(x, cnt=0, pos=0):
    res = 0
    dpl = False
    flag = x in que
    for i in tree[x]:
        if i == pos:continue
        k = bfs(i, cnt+1, x)
        res += k
        if k != 0:
            if dpl:
                res -= cnt
            else:
                dpl = True
    if flag and res == 0: res += cnt
    return res

n = int(input())
tree = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
q = int(input())
ans = [0] * q
for i in range(q):
    que = list(map(int, input().split()))
    que.pop(0)
    start = que.pop(0)
    que = set(que)
    ans[i] = bfs(start)
for i in ans:
    print(i)