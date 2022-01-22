import itertools
import numpy as np
N,X=map(int,input().split())
L=[0]*N
count=0
for i in range(N):
    LIST=list(map(int,input().split()))
    del LIST[0]
    L[i]=LIST
for a in itertools.product(*L):
    if np.prod(a)==X:count+=1
print(count)