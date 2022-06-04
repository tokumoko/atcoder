n, k = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(a)
d = [dict() for _ in range(k)]
for i in range(n):
    if d[i%k].get(b[i], -1) == -1:
        d[i%k][b[i]] = 0
    d[i%k][b[i]] += 1
flag = True
for i in range(n):
    if d[i%k].get(a[i], 0) == 0:
        flag = False
    else:
        d[i%k][a[i]] -= 1
print('Yes' if flag else 'No')