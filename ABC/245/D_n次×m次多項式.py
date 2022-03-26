n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
a.reverse()
c.reverse()
b = [0] * (m + 1)
for i in range(m+1):
    b[i] = c[i] // a[0]
    for j in range(1, n+1):
        c[i + j] -= b[i] * a[j]
b.reverse()
print(*b)