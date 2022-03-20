n, m = map(int, input().split())
a = list(map(int, input().split()))
s = []
for i in range(3):
    s.append('{:b}'.format(a[i]))
print(s)
for i in range(10):
    b = []
    c = []
    k = 0
    for j in range(3):
        k ^= int(s[j],2)
        b.append('{:b}'.format(k))
        c.append(k)
    s = b
    print(s,c)