from fractions import Fraction
import numpy as np
N=int(input())
l=[[0]]*N
ans=[]
for i in range(N):
    l[i]=np.array(list(map(int,input().split())))
    for j in range(i):
        b=l[i][1]-l[j][1]
        if b!=0:
            a=Fraction(l[i][0]-l[j][0],b)
            ans.append(str(a))
        else :
            ans.append('∞')
print(len(set(ans))*2)