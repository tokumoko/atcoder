n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans1 = 0
ans2 = 0
d = {}
for i in range(n):
    d[b[i]] = i
for i in range(n):
    k = d.get(a[i], -1)
    if k == i:ans1 += 1
    elif k != -1:ans2 += 1
print(ans1)
print(ans2)