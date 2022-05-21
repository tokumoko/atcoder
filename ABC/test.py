import heapq


a = [(2, 12), (32, 2), (3, 3)]
heapq.heapify(a)
print(heapq.heappop(a))
print(heapq.heappop(a))
print(heapq.heappop(a))