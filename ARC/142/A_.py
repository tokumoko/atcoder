n, k = map(int, input().split())
s = list(str(k))
s.reverse()
nk = int(''.join(s))
if k > nk:
    print(0)
    exit()
ans = 0
while k <= n:
    ans += 1
    k *= 10
while nk <= n:
    ans += 1
    nk *= 10
if k == nk:ans //= 2
print(ans)