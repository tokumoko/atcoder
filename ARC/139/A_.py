n = int(input())
t = list(map(int, input().split()))
ans = 0
for i in range(n):
    val = 2 ** t[i]
    if ans < val:
        ans = val
    else:
        k = ans % val
        ans += val - k
        if ans % (val*2) == 0:
            ans += val
print(ans)        