n, k = map(int, input().split())
s = list(input())
for i in range(1, n):
    if n % i != 0:continue
    ans = 0
    for count in range(i):
        d = dict()
        for j in range(count, n, i):
            if s[j] not in d:
                d[s[j]] = 0
            d[s[j]] += 1
        val = 0
        for res in d:
            if d[res] > val:
                ans += val
                val = d[res]
            else:
                ans += d[res]
    if ans <= k:
        print(i)
        exit()
print(n)