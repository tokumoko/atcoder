n = int(input())
s = input()
w = list(map(int, input().split()))
p = []
res = 0
for i in range(n):
    if s[i] == '0':
        p.append((w[i], 0))
    else:
        res += 1
        p.append((w[i], 1))
p.sort()
ans = res
for i in range(n):
    if p[i][1] == 0:
        res += 1
    else:
        res -= 1
    if i != n-1 and p[i][0] == p[i+1][0]:
        continue
    ans = max(ans, res)
print(ans)