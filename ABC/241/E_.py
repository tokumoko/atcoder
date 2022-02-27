from functools import lru_cache
@lru_cache
def f(x):
    return a[x]

n,k=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(k):
    s+=f(s%n)
print(s)