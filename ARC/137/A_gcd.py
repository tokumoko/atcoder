from math import gcd
L, R = map(int, input().split())
cnt = 0
for i in range(R-L, 0, -1):
    cnt += 1
    l = L
    r = R
    for j in range(cnt):
        if j == 0:
            r -= cnt-1
        else:
            l += 1
            r += 1
        if gcd(l, r) == 1:
            print(i)
            exit()