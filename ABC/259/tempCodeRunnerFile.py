from cmath import pi
import math
a, b, d = map(int, input().split())
c = math.sqrt(a*a + b*b)
x = math.cos(math.acos(a/c) + math.radians(d))
y = math.sin(math.asin(b/c) + math.radians(d))
print(x * c, y * c)