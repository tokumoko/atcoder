from math import ceil
n, a, b = map(int, input().split())
s = list(map(int, input().split()))
l = 1
r = (sum(s) // n) + 1
while l+1 < r:
    c = (l + r) // 2
    plus = 0
    minus = 0
    for i in s:
        if i < c:
            plus += ceil((c-i) / a)
        else:
            minus += (i-c) // b
    if plus > minus:
        r = c
    else:
        l = c
print(l)