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
    for j in range(1, len(sn)):
        if len(sn) % j != 0:continue
        val = int(sn[:j])
        res = f(val, len(sn))
        if res > n:
            if val == 1 or len(str(val)) != len(str(val - 1)):
                res = f(9, len(sn) - 1)
            else:
                res = f(val-1, len(sn))
        if n >= res:
            ans = max(ans, res)
    print(ans)