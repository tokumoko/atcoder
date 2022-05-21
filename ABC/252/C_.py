n = int(input())
slot = [[0] * 10 for _ in range(10)]
for i in range(n):
    s = input()
    for j in range(10):
        slot[int(s[j])][j] += 1
ans = 10**9
for i in range(10):
    ind = 0
    lrg = 0
    for j in range(10):
        if slot[i][j] >= lrg:
            lrg = slot[i][j]
            ind = j
    ans = min(ans, (lrg-1)*10 + ind)
print(ans)