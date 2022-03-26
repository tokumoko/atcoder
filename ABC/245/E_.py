n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
a,b = zip(*sorted(zip(a,b)))
c,d = zip(*sorted(zip(c,d)))
i = 0
j = 0
flag = True
for i in range(n):
    if j >= m:
        print('No')
        exit()
    while a[i] > c[j] or b[i] > d[j]:
        j += 1
        if j >= m:
            print('No')
            exit()
    j += 1
print('Yes')