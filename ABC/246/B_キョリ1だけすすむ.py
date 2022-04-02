from math import sqrt
a, b = map(int, input().split())
d = sqrt(a*a + b*b)
print(a / d, b / d)