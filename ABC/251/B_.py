n, w = map(int, input().split())
a = list(map(int, input().split()))
ans = set()
for i in range(n):
    if a[i] <= w:
        ans.add(a[i])
    for j in range(i+1, n):
        if a[i] + a[j] <= w:
            ans.add(a[i] + a[j])
        for k in range(j+1, n):
            if a[i] + a[j] + a[k] <= w:
                ans.add(a[i] + a[j] + a[k])
print(len(ans))