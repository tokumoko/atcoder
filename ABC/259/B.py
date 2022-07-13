import math
a, b, d = map(int, input().split())
c = math.sqrt(a*a + b*b)
if c == 0:
    print(0, 0)
    exit()
if b > 0 or (a > 0 and b == 0):
    x = math.cos(math.acos(a/c) + math.radians(d))
else:
    x = math.cos(math.acos(a/c) - math.radians(d))
if a > 0 or (a == 0 and b < 0):
    y = math.sin(math.asin(b/c) + math.radians(d))
else:
    y = math.sin(math.asin(b/c) - math.radians(d))
print(x * c, y * c)