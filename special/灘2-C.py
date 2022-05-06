n, k = map(int, input().split())
p = n // 2
k -= n - p
mod = 998244353
if k < 0:
    print(0)
    exit()
ans = 1
for i in range(1, k+1):
    ans *= p
    ans /= i
    p -= 1
    ans %= mod
print(int(ans))