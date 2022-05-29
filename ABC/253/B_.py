h, w = map(int, input().split())
t = []
for i in range(h):
    s = list(input())
    for j in range(w):
        if s[j] == 'o':
            t.append((i, j))
print(abs(t[0][0] - t[1][0]) + abs(t[0][1] - t[1][1]))