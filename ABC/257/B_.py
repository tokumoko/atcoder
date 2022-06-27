n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))
for i in range(q):
    val = a[l[i] - 1]
    if val < n and (l[i] == k or a[l[i]] != val+1):
        a[l[i]-1] += 1
print(*a)