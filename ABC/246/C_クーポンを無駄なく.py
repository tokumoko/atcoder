n, k, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    t = a[i] // x
    t = min(k, t)
    a[i] -= t * x
    k -= t
    ans += a[i]
if k != 0:
    a.sort(reverse=True)
    for i in range(min(len(a), k)):
        ans -= a[i]
print(ans)