n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = [0] * (n+1)
now = int(input())
for i in range(m-1):
    nxt = int(input())
    if now < nxt:
        b[now] += 1
        b[nxt] -= 1
    else:
        b[nxt] += 1
        b[now] -= 1
    now = nxt
now = 0
ans = 0
for i in range(1,n):
    now += b[i]
    ans += now * a[i-1]
print(ans)