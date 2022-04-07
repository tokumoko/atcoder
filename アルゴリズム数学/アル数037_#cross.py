def normal():
    a = (y[1] - y[0]) / (x[1] - x[0])
    b = y[0] - a*x[0]
    c = (y[3] - y[2]) / (x[3] - x[2])
    d = y[2] - c*x[2]
    e = max(x[0], x[2])
    f = min(x[1], x[3])
    if e > f:return False
    y0 = a * e + b
    y1 = a * f + b
    y2 = c * e + d
    y3 = c * f + d
    if (y0 >= y2 and y1 <= y3) or (y0 <= y2 and y1 >= y3):
        return True
    return False
x = [0] * 4
y = [0] * 4
for i in range(4):
    x[i], y[i] = map(int, input().split())
if x[0] > x[1] or (x[0] == x[1] and y[0] > y[1]):
    x[0], x[1] = x[1], x[0]
    y[0], y[1] = y[1], y[0]
if x[2] > x[2] or (x[2] == x[3] and y[2] > y[3]):
    x[2], x[3] = x[3], x[2]
    y[2], y[3] = y[3], y[2]
if x[1] != x[0] and x[2] != x[3]:
    ans = normal()
elif x[0] == x[1] and x[2] == x[3]:
    ans = False
elif x[0] == x[1]:
    c = (y[3] - y[2]) / (x[3] - x[2])
    d = y[2] - c*x[2]
    n = c * x[0] + d
    if y[0] <= n <= y[1] and x[2] <= x[0] <= x[3]:
        ans = True
    else:
        ans = False
else:
    a = (y[1] - y[0]) / (x[1] - x[0])
    b = y[0] - a*x[0]
    n = a * x[2] + b
    if y[2] <= n <= y[3] and x[0] <= x[2] <= x[1]:
        ans = True
    else:
        ans = False
print('Yes' if ans else 'No')