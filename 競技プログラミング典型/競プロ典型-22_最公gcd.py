from math import gcd
a,b,c=map(int,input().split())
n=gcd(gcd(a,b),c)
a//=n;b//=n;c//=n
print(a+b+c-3)