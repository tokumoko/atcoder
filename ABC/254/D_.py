from math import sqrt
n = int(input())
ans = 1
for i in range(2, n+1):
    t = 0
    for j in range(2, int(sqrt(i)+1)):
        if i % j == 0:
            t = j
            break
    if t == 0:t = i
    a = i*i
    ans += 1
    while a <= n:
        ans += 2
        a *= t
print(ans)