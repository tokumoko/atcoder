x, y = map(int, input().split())
mod = 10**9 + 7
a = [0] * (x+y+1)
a[0] = 1
for i in range(1, x+y+1):
    a[i] = (a[i-1] * i) % mod
print(a[x+y] * pow(a[x]*a[y], mod-2, mod)%mod)