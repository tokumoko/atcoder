from math import gcd
n = int(input())
k, m = map(int, input().split())
p = m // gcd(k, m)
if n % p == 0:
    print('Yes')
else:
    print('No')