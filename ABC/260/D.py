n, k = map(int, input().split())
p = list(map(int, input().split()))
eat = [-1] * n
for i in range(n):
    if eat[p[i]] != -1:continue
    x = p[i]
    deck = [x]
    for j in range(i+1, n):
        if eat[p[j]] != -1:continue
        if x > p[j]:
            x = p[j]