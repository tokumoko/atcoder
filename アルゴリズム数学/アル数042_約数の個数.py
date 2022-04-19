n = int(input())
cnt = [0] * (n+1)
ans = 0
for i in range(1,n+1):
    for j in range(i, n+1, i):
        cnt[j] += 1
    ans += i * cnt[i]
print(ans)