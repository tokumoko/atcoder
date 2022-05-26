mod = 10**9 + 7
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
n = int(input()) - 1
ans = [1, 1]
r = [[2, 1], [1, 0]]
while n > 0:
    if n % 2 == 1:
        ans = g(r, ans)
    n >>= 1
    r = f(r, r)
print(ans[1])