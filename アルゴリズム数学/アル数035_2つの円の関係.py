from math import sqrt
a, b, r = map(int, input().split())
c, d, l = map(int, input().split())
dis = r+l
sid = abs(r-l)
distance = sqrt((c - a)*(c - a) + (d - b)*(d - b))
if distance < sid:
    ans = 1
elif distance == sid:
    ans = 2
elif distance < dis:
    ans = 3
elif distance == dis:
    ans = 4
elif distance > dis:
    ans = 5
print(ans)