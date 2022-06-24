n = int(input())
x = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
discover = [0] * (n + 1)
cnt = 0
ans = 0
for i in range(1, n+1):
    if discover[i] != 0:continue
    cnt += 1
    while discover[i] == 0:
        discover[i] = cnt
        i = x[i]
    if discover[i] == cnt:
        st = i
        i = x[i]
        res = c[st]
        while i != st:
            res = min(res, c[i])
            i = x[i]
        ans += res
print(ans)