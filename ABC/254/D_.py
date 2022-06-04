from math import sqrt
n = int(input())
ans = 0
for i in range(1, n+1):
    k = i
    for j in range(2, int(sqrt(n)+1)):
        while k % (j*j) == 0:k //= j*j
    for j in range(1, n+1):
        if k*j*j > n:break
        ans += 1
print(ans)