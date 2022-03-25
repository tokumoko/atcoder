from itertools import permutations
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
uwasa = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    uwasa[x].append(y)
    uwasa[y].append(x)
ans = 10**9
for p in permutations(range(n),n):
    flag = True
    for i in range(n-1):
        if p[i+1] in uwasa[p[i]]:
            flag = False
    if flag:
        score = 0
        for i in range(n):
            score += a[p[i]][i]
        if ans > score:
            ans = score
if ans == 10 ** 9:ans = -1
print(ans)