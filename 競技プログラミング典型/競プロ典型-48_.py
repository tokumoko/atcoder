import heapq


n, k = map(int, input().split())
p = [0] * n
que = []
heapq.heapify(que)
for i in range(n):
    a, b = map(int, input().split())
    p[i] = b - a
    heapq.heappush(que, (-b, i))
ans = 0
for i in range(k):
    x, ind = heapq.heappop(que)
    ans -= x
    if ind != -1:
        heapq.heappush(que, (p[ind], -1))
print(ans)