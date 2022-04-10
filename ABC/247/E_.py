n, x, y = map(int, input().split())
a = list(map(int, input().split()))
ind = []
for i in range(n):
    if a[i] == x:
        ind.append((x, i))
    if a[i] == y:
        ind.append((y, i))
    if a[i] > x or a[i] < y:
        ind.append((0, i))
ans = 0
for i in range(len(ind)):
    if ind[i][0] == 0:continue
    if x == ind[i][0]:val = y
    else:val = x
    rs = -1
    j = i
    flag = False
    while j < len(ind):
        if ind[j][0] == val:
            rs = ind[j][1]
            break
        if ind[j][0] == 0:
            flag = True
            break
        j += 1
    if flag or rs == -1:continue
    j += 1
    if j == len(ind):
        ans += 1
        continue
    rg = -1
    while j < len(ind):
        if ind[j][0] == 0:
            rg = ind[i][1] - 1
            break
        j += 1
    if rg == -1:rg = n-1
    print(i, rs, rg)
    ans += (j-1) - rs
print(ans)