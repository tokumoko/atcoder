from bisect import bisect_left, bisect_right
n = int(input())
a = list(map(int, input().split()))
b = [[] for _ in range(n + 1)]
q = int(input())
for i in range(n):
    b[a[i]].append(i)
for i in range(q):
    l, r, x = map(int, input().split())
    l -= 1
    r -= 1
    l_ind = bisect_left(b[x], l)
    r_ind = bisect_right(b[x], r)
    print(r_ind - l_ind)