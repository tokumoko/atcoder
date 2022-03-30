from math import gcd
a, b = map(int, input().split())
ans = a * b // gcd(a,b)
if ans > 10 ** 18:
    print('Large')
else:
    print(ans)