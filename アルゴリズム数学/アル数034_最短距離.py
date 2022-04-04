from math import sqrt
n = int(input())
x = [0] * n
y = [0] * n
ans = 10**18
for i in range(n):x[i], y[i] = map(int, input().split())
for i in range(n-1):
    for j in range(i+1,n):
        res = (x[j] - x[i])**2 + (y[j] - y[i])**2
        ans = min(ans, res)
print(sqrt(ans))