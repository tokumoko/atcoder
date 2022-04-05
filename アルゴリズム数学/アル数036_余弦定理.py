from math import cos, radians, sqrt
a, b, h, m = map(int, input().split())
tan = h * 30 + m / 2
tyo = m * 6
ans = a*a + b*b - 2*a*b*cos(radians(abs(tan - tyo)))
print(sqrt(ans))