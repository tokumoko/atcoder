n, k = map(int, input().split())
a = list(map(int, input().split()))
if sum(a) <= k and sum(a) % 2 == k % 2:
    print('Yes')
else:
    print('No')