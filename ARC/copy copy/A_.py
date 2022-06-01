def f(x, l):
    t = len(str(x))
    ans = 0
    for i in range(0, l, t):
        ans += x * (10**i)
    return ans

t = int(input())
for i in range(t):
    n = int(input())
    sn = str(n)
    ans = 0
    for j in range(1, len(sn) + 1):
        if n % j != 0:continue
        val = int(sn[:j])
        res = f(val, len(sn))
        if res > n:
            res = f(val-1, len(sn))
        ans = max(ans, res)
    print(ans)