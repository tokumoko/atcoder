def get_grundy(x, y):
    if grundy[x][y] != -1:
        return grundy[x][y]
    l = [False] * 700
    if x != 0 and y+x < 1326:
        l[grundy[x-1][y+x]] = True
    for i in range((y+1) // 2, y):
        l[grundy[x][i]] = True
    i = 0
    while l[i] : i += 1
    return i
grundy = [[-1] * 1326 for _ in range(51)]
grundy[0][0] = 0
grundy[0][1] = 0
for i in range(51):
    for j in range(1326):
        grundy[i][j] = get_grundy(i, j)
n = int(input())
w = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans ^= grundy[w[i]][b[i]]
print('First' if ans != 0 else 'Second')