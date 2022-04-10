n = int(input())
a = list(map(int, input().split()))
b = sorted(a,reverse=True)
c = sorted(a)
d = dict()
for i in range(n):
    d[c[i]] = i
for i in range(n):
    a[i] = d.get(a[i])
s = sum(b[:n//2])
val = 0
res = 10**18
ind = 0
for i in range(n):
    if a[i] < n//2:
        val += 1
    else:
        val -= 1
    if res > val:
        res = val
        ind = i
print(ind, s)