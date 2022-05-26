n, m = map(int, input().split())
p = [[] for _ in range(n)]
for i in range(n):
    c, l, r = map(int, input().split())
    p[l].append(r, c)