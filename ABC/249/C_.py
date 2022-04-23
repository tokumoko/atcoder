n, k = map(int, input().split())
s = [list(input()) for _ in range(n)]
ans = 0
for i in range(2**n):
    b='{:b}'.format(i)
    b = b.zfill(n)
    d = dict()
    res = 0
    for j in range(n):
        if b[j] == '1':
            for l in s[j]:
                if d.get(l, 0) == 0:
                    d[l] = 1
                else:
                    d[l] += 1
    for j in d:
        if d[j] == k:
            res += 1
    if ans < res:
        ans = res
print(ans)