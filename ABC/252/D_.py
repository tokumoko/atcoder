n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in range(n):
    if d.get(a[i], -1) == -1:
        d[a[i]] = 0
    d[a[i]] += 1
ans = n*(n-1)*(n-2) // 6
n -= 2
for i in d:
    if d[i] < 2:continue
    num = d[i]*(d[i]-1)*(d[i]-2) // 6
    d[i] -= 1
    k = (1 + d[i])*d[i] // 2
    ans -= (n - d[i] + 1) * k + num
print(ans)