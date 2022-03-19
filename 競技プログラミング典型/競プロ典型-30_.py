n, k = map(int, input().split())
cnt = [0] * (n+1)
prime = [True] * (n+1)
prime[0] = prime[1] = False
ans = 0
for i in range(2,n+1):
    if prime[i]:
        for j in range(i, n+1, i):
            cnt[j] += 1
            prime[j] = False
    if cnt[i] >= k:ans += 1
print(ans)