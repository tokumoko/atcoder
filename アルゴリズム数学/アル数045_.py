n, m = map(int, input().split())
t = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    t[a].append(b)
    t[b].append(a)
ans = 0
for i in range(n):
    flag = False
    for j in t[i]:
        if i > j and flag:
            flag = False
            break
        elif i > j:
            flag = True
    if flag:
        ans += 1
print(ans)