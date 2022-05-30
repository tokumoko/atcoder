def f(a, b):
    ans = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][k] += a[i][j] * b[j][k]
                ans[i][k] %= mod
    return ans
def g(a, b):
    ans = [0, 0]
    for i in range(2):
        for j in range(2):
            ans[i] += a[i][j] * b[j]
            ans[i] %= mod
    return ans
def fib(x, r):
    ans = [1, 0]
    while x > 0:
        if x % 2 == 1:
            ans = g(r, ans)
        x >>= 1
        r = f(r, r)
    return ans[0]
k, n = map(int, input().split())
mod = 10**9 + 7
if k == 2:
    print(fib(n, [[1, 1], [1, 0]]))
elif k == 3:
    if n % 2 == 0:
        print(fib(n, [[1, 1], [1, 0]]))
        #0, 3, 0, 11, 6+12+8+4+
    else:
        print(0)
if k == 4:
    print(fib(n, [[1, 1], [1, 0]]))