x, y = map(int, input().split())
mod = 10**9 + 7
if x > y: x, y = y, x
m = y-x
x -= m
y -= m*2
if x % 3 != 0 or x < 0:
    print(0)
    exit()
n = x // 3
m += n
a = [0] * (n + m + 1)
a[0] = 1
for i in range(1, n+m+1):
    a[i] = (a[i-1] * i) % mod
print(a[n+m] * pow(a[n]*a[m], mod-2, mod)%mod)