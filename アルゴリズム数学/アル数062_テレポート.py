n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
c = []
d = dict()
ind = 1
cnt = 0
while d.get(ind, -1) == -1:
    d[ind] = cnt
    c.append(ind)
    ind = a[ind]
    cnt += 1
if k < d[ind]:
    print(c[k])
else:
    k -= d[ind]
    mod = cnt - d[ind]
    print(c[(k % mod) + d[ind]])