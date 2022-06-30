n = int(input())
c = [n+1] + list(map(int, input().split()))
m = min(c)
k = n // m
ans = []
for a in range(1, k+1):
    for i in range(9, 0, -1):
        if k-a == (n - c[i]) // m and n - c[i] >= 0:
            n -= c[i]
            ans.append(str(i))
print(''.join(ans))