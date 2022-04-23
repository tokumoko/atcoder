n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in a:
    if d.get(i, -1) == -1:
        d[i] = 0
    d[i] += 1
a.sort()
a = set(a)
val = max(a)
ans = 0
print(d)
for i in a:
    for j in a:
        ans += d.get(i*j, 0) * d[i] * d[j]
        if i*j > val:break
print(ans)