n, k = map(int, input().split())
a = list(map(int, input().split()))
use = dict()
dlt = 0
cnt = 0
ans = 0
for i in range(n):
    if a[i] not in use:
        use[a[i]] = 0
    use[a[i]] += 1
    cnt += 1
    while len(use) > k:
        use[a[dlt]] -= 1
        if use[a[dlt]] == 0:
            use.pop(a[dlt])
        dlt += 1
        cnt -= 1
    if ans < cnt : ans = cnt
print(ans)