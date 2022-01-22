import numpy as np
S=list(input())
T=list(input())
A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
i=0
N=len(S)
s=np.array([0]*N)
t=np.array([0]*N)
for i in range(N):
    s[i]=A.index(S[i])
    t[i]=A.index(T[i])
l=s[0]-t[0]
ans="Yes"
for i in range(N):
    if s[i]!=(t[i]+l)%26:ans="No"
print(ans)