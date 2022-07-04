n = int(input())
a = [list(input()) for _ in range(n)]
b = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        b[i][j] = int(a[i][j])
p = [-1, 0, 1]
ans = 0
for x in p:
    for y in p:
        if x == y == 0:continue
        for i in range(n):
            for j in range(n):
                res = 0
                for t in range(n-1, -1, -1):
                    res += 10**t * b[i][j]
                    i += y
                    j += x
                    if i < 0:i += n
                    if j < 0:j += n
                    i %= n
                    j %= n
                ans = max(res, ans)
print(ans)