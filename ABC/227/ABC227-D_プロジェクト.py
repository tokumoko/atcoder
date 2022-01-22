import numpy as np
n,k=map(int, input().split())
a=np.array(list(map(int, input().split())))
s=0
b=np.amax(a)
while b*k>np.sum(a):
    b-=1
    for i in range(n):
        if a[i]>b:
            a[i]=b
print(b)