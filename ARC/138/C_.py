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

print(a)