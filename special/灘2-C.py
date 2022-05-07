n, k = map(int, input().split())
k = n - k
n //= 2
k = n - k
if k < 0:
    print(0)
    exit()
mod = 998244353
ans = 1
for i in range(1, k+1):
    ans *= n
    ans /= i
    n -= 1
    ans %= mod
print(int(ans))