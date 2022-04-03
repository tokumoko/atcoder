from math import sqrt
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
x = cy - by
y = bx - cx
m = -bx*x - by*y
d = (abs(ax*x + ay*y + m)) / (sqrt(x*x + y*y))
e = sqrt((ax - bx)*(ax - bx) + (ay - by)*(ay - by))
f = sqrt((ax - cx)*(ax - cx) + (ay - cy)*(ay - cy))
n = x*ax - ay*y
print(x, y, n, m)
kouteny = (m + n) / 2
koutenx = -(kouteny * y + m)
print(koutenx, kouteny)