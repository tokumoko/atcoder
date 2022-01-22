import heapq
N,K=map(int,input().split())
P=list(map(int,input().split()))
L=P[:K]
heapq.heapify(L)
a=heapq.heappop(L)
print(a)
for i in range(K,N):
    if P[i]>a:
        heapq.heappush(L,P[i])
        a=heapq.heappop(L)
    print(a)