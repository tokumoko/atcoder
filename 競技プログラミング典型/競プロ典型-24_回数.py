n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
score = 0
for i in range(n):
    score += abs(a[i]-b[i])
if k >= score and (k - score)%2 == 0:
    print('Yes')
else:
    print('No')