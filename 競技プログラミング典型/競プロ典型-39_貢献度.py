import sys
sys.setrecursionlimit(1000000)
def dfs(x, pos=0):
    global ans
    cnt = 0
    for i in tree[x]:
        if i != pos:
            cnt += dfs(i, x)
    cnt += 1
    ans += cnt * (n-cnt)
    return cnt

n = int(input())
tree = [[] for _ in range(n)]
ans = 0
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)
dfs(0)
print(ans)